# -*- coding: utf-8 -*-
"""
步骤B — DeepSeek 语言重判器
对 vocabulary_v3.json 每条,在 ep_langs 候选内判真实 ISO 语言。
候选约束 = 强先验(候选已缩至 3-6/集),准确率高。
批量(默认 20/请求)+ 断点续传(已判条带 lang_new,重跑跳过)+ --limit 测试。

用法:
  python ep_relang.py --limit 60      # 先测 60 条
  python ep_relang.py --all           # 全量(可重复跑,自动续传)
key 从 .env 读,绝不硬编码。
"""
import json, os, sys, time, urllib.request, urllib.error

SRC = "vocabulary_v3.json"
OUT = "vocabulary_v4.json"
API = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"
BATCH = 20
FLUSH_EVERY = 5  # 每 5 批写盘一次(断点续传)

ISO_DESC = {
    "en": "英语", "es": "西班牙语", "fr": "法语", "yue": "粤语(含唔/嘅/咗/啲或jyutping拼音)",
    "el": "希腊语(可能罗马转写)", "nl": "荷兰语", "id": "印尼语", "ja": "日语(可能罗马音)",
    "ar": "阿拉伯语(可能罗马转写)", "zh": "普通话中文",
}


def load_key():
    for line in open(".env", encoding="utf-8"):
        if line.startswith("DEEPSEEK_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("no DEEPSEEK_API_KEY in .env")


def build_prompt(batch):
    cand = sorted({L for x in batch for L in x["ep_langs"]})
    legend = "  ".join(f"{k}={ISO_DESC.get(k,k)}" for k in cand)
    lines = []
    for i, x in enumerate(batch):
        allow = "/".join(x["ep_langs"])
        lines.append(f'{i}\tword="{x["word"]}"\tdef="{x["def"][:40]}"\t候选={allow}')
    body = "\n".join(lines)
    return (
        "你是严谨的语言鉴定器。释义是中文,词形(word)是目标语言。\n"
        f"ISO代码含义: {legend}\n"
        "规则:\n"
        "- 每条只能从该条给出的「候选」里选一个 ISO 代码,严禁选候选外的。\n"
        "- 看 word 词形特征 + 中文释义综合判断(如法/西/英/印尼/荷兰拉丁字母相近,靠词尾/拼写/词源辨别)。\n"
        "- 粤语 yue: word 含唔嘅咗啲乜嘢等粤字,或含 jyutping(如 lo/saai/zo)。\n"
        "- 拿不准时选候选中最可能者,conf 给低分。\n"
        f"逐条判定以下 {len(batch)} 条,返回纯 JSON 数组,每元素 {{\"i\":序号,\"lang\":\"iso\",\"conf\":0.0-1.0}},不要任何额外文字:\n"
        + body
    )


def call(key, prompt, retries=4):
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "response_format": {"type": "json_object"},
        "max_tokens": 4000,
    }
    data = json.dumps(payload).encode()
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                API, data=data,
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=180) as r:
                raw = r.read()  # 先全量读,避 chunked 截断 IncompleteRead
            resp = json.loads(raw)
            return resp["choices"][0]["message"]["content"], resp.get("usage", {})
        except Exception as e:  # 网络/截断/解析皆重试
            last = e
            time.sleep(2 * (attempt + 1))
    raise last


def parse_arr(txt):
    txt = txt.strip()
    if txt.startswith("```"):
        txt = txt.strip("`").split("\n", 1)[-1]
    obj = json.loads(txt)
    if isinstance(obj, dict):
        for v in obj.values():
            if isinstance(v, list):
                return v
        return [obj]
    return obj


def main():
    mode_all = "--all" in sys.argv
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])

    key = load_key()
    # 续传:若 OUT 已存在,从它读(保留已判 lang_new)
    data = json.load(open(OUT if os.path.exists(OUT) else SRC, encoding="utf-8"))

    todo = [i for i, x in enumerate(data) if not x.get("lang_new")]
    if limit:
        todo = todo[:limit]
    print(f"待判 {len(todo)} 条(总 {len(data)},已判 {len(data)-sum(1 for x in data if not x.get('lang_new'))})")
    if not todo:
        print("全部已判,完成。")
        return

    tot_in = tot_out = 0
    done = 0
    for b in range(0, len(todo), BATCH):
        idxs = todo[b:b + BATCH]
        batch = [data[i] for i in idxs]
        try:
            txt, usage = call(key, build_prompt(batch))
            arr = parse_arr(txt)
            tot_in += usage.get("prompt_tokens", 0)
            tot_out += usage.get("completion_tokens", 0)
            by_i = {int(o["i"]): o for o in arr if "i" in o}
            for local, gi in enumerate(idxs):
                o = by_i.get(local)
                if o and o.get("lang") in data[gi]["ep_langs"]:
                    data[gi]["lang_new"] = o["lang"]
                    data[gi]["conf"] = round(float(o.get("conf", 0)), 2)
                else:
                    # 模型越界或缺漏:回退到候选第一个,标记低信心
                    data[gi]["lang_new"] = (o.get("lang") if o else data[gi]["ep_langs"][0])
                    data[gi]["conf"] = 0.0
            done += len(idxs)
        except Exception as e:  # 兜底:任何批失败都跳过,下次续传重试,不崩整跑
            print(f"  批 {b//BATCH} 出错: {type(e).__name__} {e},跳过(下次续传重试)")
            time.sleep(2)
            continue
        if (b // BATCH) % FLUSH_EVERY == 0:
            json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            print(f"  进度 {done}/{len(todo)}  in={tot_in} out={tot_out}")

    json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    # DeepSeek 定价(chat,缓存未命中约 in $0.27/M, out $1.10/M;以此估)
    cost = tot_in / 1e6 * 0.27 + tot_out / 1e6 * 1.10
    print(f"\n完成 {done} 条。tokens in={tot_in} out={tot_out}  约 ${cost:.4f} USD")


if __name__ == "__main__":
    main()
