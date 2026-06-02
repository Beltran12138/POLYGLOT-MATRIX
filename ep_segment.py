# -*- coding: utf-8 -*-
"""
EP 切分器 — 步骤A
把 vocabulary.json 按 EP 标题行(文件边界)切分,为每条词条打 ep 号 + 该集声明语言。
纯规则,零 API。只生成新文件 vocabulary_v3.json,不动原数据。
段内原始顺序已被字母排序覆盖(不可逆),故只恢复到「集级」粒度。
"""
import json
import re
import os
import collections

SRC = "vocabulary.json"
OUT = "vocabulary_v3.json"

# 标题里的语言名 -> ISO 639(粤语用 yue)
LANG_MAP = {
    "english": "en", "español": "es", "espanol": "es",
    "français": "fr", "francais": "fr",
    "cantonese": "yue", "粵語": "yue", "粤语": "yue",
    "ελληνικά": "el",                       # 希腊语
    "nederland": "nl", "nederlands": "nl",  # 荷兰语
    "العربية": "ar",                        # 阿拉伯语
    "bahasa indonesia": "id", "bahasa": "id", "indonesia": "id",
    "日本語": "ja",
}

EP_RE = re.compile(r"EP\s?(\d+)", re.IGNORECASE)


def parse_title(text):
    """从 EP 标题行解析 (ep_num, [iso langs])。非标题返回 None。"""
    m = EP_RE.search(text)
    if not m:
        return None
    ep = int(m.group(1))
    body = EP_RE.sub("", text)
    langs = []
    # 先抓非 ASCII 整词(希腊/阿拉伯/中文/日文)
    for key in ("粵語", "粤语", "ελληνικά", "العربية", "日本語", "bahasa indonesia"):
        if key in body.lower() if key.isascii() else key in body:
            iso = LANG_MAP[key]
            if iso not in langs:
                langs.append(iso)
    # 再按分隔符拆 ASCII 语言名
    for tok in re.split(r"[&,/]| and ", body):
        t = tok.strip().lower()
        if t in LANG_MAP and LANG_MAP[t] not in langs:
            langs.append(LANG_MAP[t])
    return ep, langs


def main():
    d = json.load(open(SRC, encoding="utf-8"))
    N = len(d)

    # 1) 定位所有 EP 标题行的 index
    titles = []  # (idx, ep, langs, raw)
    for i, x in enumerate(d):
        raw = (x.get("word", "") + " " + x.get("def", "")).strip()
        p = parse_title(raw)
        if p:
            titles.append((i, p[0], p[1], raw))

    print(f"源词条 {N} 条,EP 标题 {len(titles)} 个")

    # 2) 用相邻标题 index 区间,给词条归集
    out = []
    cur_ep, cur_langs = None, []
    title_idx = {i for i, *_ in titles}
    # idx -> (ep,langs) 在标题处切换
    boundary = {i: (ep, langs) for i, ep, langs, _ in titles}

    seg_counter = collections.Counter()
    for i, x in enumerate(d):
        if i in boundary:
            cur_ep, cur_langs = boundary[i]
            continue  # 标题行本身不作为词条(剔除)
        rec = {
            "word": x.get("word", ""),
            "type": x.get("type", ""),
            "def": x.get("def", ""),
            "lang_old": x.get("lang", ""),   # 旧的(待步骤B重判)
            "ep": cur_ep,                     # 所属集(None=EP标题前的孤儿)
            "ep_langs": cur_langs,            # 该集声明语言候选
        }
        out.append(rec)
        seg_counter[cur_ep] += 1

    # 3) 落盘
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"写出 {OUT}:{len(out)} 条词条(已剔除 {len(titles)} 行标题)")

    # 4) 报告:每集词数 + 声明语言
    print("\n=== 每集词条数(按 EP 号排序) ===")
    ep_langs_map = {ep: langs for _, ep, langs, _ in titles}
    orphan = seg_counter.get(None, 0)
    for ep in sorted(k for k in seg_counter if k is not None):
        langs = ep_langs_map.get(ep, [])
        print(f"  EP{ep:<3} {seg_counter[ep]:>5} 条  langs={'/'.join(langs)}")
    if orphan:
        print(f"  (孤儿:无 EP 前缀 {orphan} 条 — 多在首个标题前)")

    # 5) 全局声明语言并集
    all_langs = collections.Counter()
    for ep, n in seg_counter.items():
        for L in ep_langs_map.get(ep, []):
            all_langs[L] += n
    print("\n=== 声明语言覆盖(按所在集词条数加权) ===")
    for L, n in all_langs.most_common():
        print(f"  {L}: 出现于覆盖 {n} 条的集中")


if __name__ == "__main__":
    main()
