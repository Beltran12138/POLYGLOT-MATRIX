# -*- coding: utf-8 -*-
"""
步骤C-A · Obsidian 双链库导出器
读 vocabulary_v4.json → 每词一 .md note(frontmatter: lang/ep/type/conf)
→ 按语言子目录组织 → 同义/同源词跨语言 [[wikilink]] 互链 → 生成 obsidian_vault/。
用法: python build_obsidian.py   →  写出 obsidian_vault/
"""
import json, collections, os, re

SRC = "vocabulary_v4.json"
VAULT = "obsidian_vault"

LANG_NAME = {
    "en": "English", "es": "Español", "fr": "Français", "yue": "粵語",
    "el": "Ελληνικά", "nl": "Nederlands", "id": "Bahasa", "ja": "日本語",
    "ar": "العربية", "zh": "中文",
}


def safe(name):
    return re.sub(r'[\\/:*?"<>|]', "_", name).strip() or "_"


def norm_def(s):
    return s.split("&")[0].split("/")[0].strip()


def main():
    d = json.load(open(SRC, encoding="utf-8"))
    d = [x for x in d if x.get("lang_new")]

    # 同义簇(用于跨语言互链):同首义 >=2 语言
    by_def = collections.defaultdict(list)
    for x in d:
        nd = norm_def(x["def"])
        if nd and len(nd) <= 8:
            by_def[nd].append(x)

    os.makedirs(VAULT, exist_ok=True)
    lang_index = collections.defaultdict(list)
    ep_index = collections.defaultdict(list)
    written = 0

    for x in d:
        L = x["lang_new"]
        ln = LANG_NAME.get(L, L)
        note_id = f"{safe(x['word'])}__{L}"      # 避跨语言同拼写冲突
        d_ = os.path.join(VAULT, ln)
        os.makedirs(d_, exist_ok=True)

        # 跨语言同源词链接
        nd = norm_def(x["def"])
        links = []
        for y in by_def.get(nd, []):
            if y is x or y["lang_new"] == L:
                continue
            links.append(f"[[{safe(y['word'])}__{y['lang_new']}|{y['word']} ({LANG_NAME.get(y['lang_new'],y['lang_new'])})]]")
        links = sorted(set(links))[:8]

        fm = (
            "---\n"
            f"word: {json.dumps(x['word'], ensure_ascii=False)}\n"
            f"lang: {L}\n"
            f"type: {json.dumps(x.get('type',''), ensure_ascii=False)}\n"
            f"conf: {x.get('conf','')}\n"
            f"tags: [lang/{L}]\n"
            "---\n"
        )
        body = (
            f"# {x['word']}\n\n"
            f"**{ln}** · {x.get('type','')}\n\n"
            f"## 释义\n{x['def']}\n\n"
        )
        if links:
            body += "## 跨语言同源\n" + "\n".join(f"- {l}" for l in links) + "\n"

        open(os.path.join(d_, note_id + ".md"), "w", encoding="utf-8").write(fm + body)
        written += 1
        lang_index[ln].append(note_id)
        if x.get("ep"):
            ep_index[x["ep"]].append((ln, x["word"], note_id))

    # 语言 MOC
    moc = ["# Polyglot Matrix — 九语库\n"]
    for ln in sorted(lang_index, key=lambda k: -len(lang_index[k])):
        moc.append(f"- **{ln}** — {len(lang_index[ln])} 词")
    open(os.path.join(VAULT, "_INDEX.md"), "w", encoding="utf-8").write("\n".join(moc))

    print(f"写出 {VAULT}/  共 {written} 条 note")
    print(f"  语言目录: {dict((k,len(v)) for k,v in lang_index.items())}")
    print(f"  EP 索引: {len(ep_index)} 集")


if __name__ == "__main__":
    main()
