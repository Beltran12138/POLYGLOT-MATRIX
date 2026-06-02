# -*- coding: utf-8 -*-
"""
步骤C-B · 学习史可视化网页生成器(全静态版)
读 vocabulary_v4.json → 聚合(语言分布 / 词性 / 跨语言同源词)→ 单 HTML。
全静态:Python 端直接生成所有内容,零 JS、零 CDN(中国可访问,必渲染)。
条形图用纯 CSS。样式 navy/金/白,反 AI slop。
用法: python build_viz.py   →  写出 index.html(Pages 入口)
"""
import json, collections, html as H

SRC = "vocabulary_v4.json"
OUT = "index.html"  # Pages 入口

LANG_NAME = {
    "en": "English", "es": "Español", "fr": "Français", "yue": "粵語",
    "el": "Ελληνικά", "nl": "Nederlands", "id": "Bahasa", "ja": "日本語",
    "ar": "العربية", "zh": "中文",
}


def norm_def(s):
    return s.split("&")[0].split("/")[0].strip()


def esc(s):
    return H.escape(str(s))


def main():
    d = [x for x in json.load(open(SRC, encoding="utf-8")) if x.get("lang_new")]
    N = len(d)

    dist = collections.Counter(x["lang_new"] for x in d)
    pos = collections.Counter()
    for x in d:
        t = x.get("type", "").strip().rstrip(".").split("/")[0].split("&")[0].strip()
        if t and len(t) <= 6:
            pos[t] += 1

    by_def = collections.defaultdict(list)
    for x in d:
        nd = norm_def(x["def"])
        if nd and len(nd) <= 8:
            by_def[nd].append((x["lang_new"], x["word"]))
    cognates = []
    for nd, items in by_def.items():
        langs = {l for l, w in items}
        if len(langs) >= 3:
            cognates.append((nd, sorted(set(items))))
    cognates.sort(key=lambda t: -len({l for l, w in t[1]}))
    conf_low = sum(1 for x in d if x.get("conf", 1) < 0.6)

    # ---- 静态生成 ----
    dist_order = dist.most_common()
    dmax = dist_order[0][1]
    dist_html = "".join(
        f'<div class="row"><span class="n">{n:,}</span>'
        f'<span class="bar" style="width:{max(2, n/dmax*420):.0f}px"></span>'
        f'<span class="lab">{esc(LANG_NAME.get(l,l))} <small>({l})</small></span></div>'
        for l, n in dist_order
    )

    pos_order = pos.most_common(12)
    pmax = pos_order[0][1] if pos_order else 1
    pos_html = "".join(
        f'<div class="row"><span class="n">{n:,}</span>'
        f'<span class="bar gold" style="width:{max(2, n/pmax*420):.0f}px"></span>'
        f'<span class="lab">{esc(t)}</span></div>'
        for t, n in pos_order
    )

    cog_html = "".join(
        f'<div class="cog"><div class="meaning">{esc(nd)}</div>'
        + "".join(f'<span class="w"><b>{esc(w)}</b> {esc(LANG_NAME.get(l,l))}</span>'
                  for l, w in items)
        + "</div>"
        for nd, items in cognates[:40]
    ) or '<div class="note">无足够跨语言同义簇</div>'

    page = TMPL.format(
        total=f"{N:,}", nlang=len(dist), ncog=len(cognates), conf_low=conf_low,
        dist=dist_html, pos=pos_html, cog=cog_html,
    )
    open(OUT, "w", encoding="utf-8").write(page)
    print(f"写出 {OUT}(全静态,无JS/CDN)")
    print(f"  总 {N} · 语言 {len(dist)} · 同源簇 {len(cognates)} · 低信心 {conf_low}")
    print("  分布:", {LANG_NAME.get(l, l): n for l, n in dist_order})


TMPL = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Polyglot Matrix · 多语词汇语料</title>
<style>
  :root{{--navy:#1B2A5A;--gold:#C9A24C;--ink:#1a1a1a;--paper:#fbfaf7;--line:#e3ddd0}}
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{background:var(--paper);color:var(--ink);font-family:"Georgia","Songti SC",serif;line-height:1.5;padding:48px 24px;max-width:1080px;margin:0 auto}}
  header{{border-bottom:3px solid var(--navy);padding-bottom:16px;margin-bottom:8px}}
  h1{{font-size:34px;color:var(--navy);letter-spacing:-.5px}}
  .sub{{color:#6b6453;font-size:13px;margin-top:6px;font-family:system-ui,sans-serif}}
  h2{{font-size:13px;letter-spacing:2px;text-transform:uppercase;color:var(--gold);
     font-family:system-ui,sans-serif;font-weight:700;margin:44px 0 14px;border-left:4px solid var(--gold);padding-left:10px}}
  .row{{display:flex;align-items:center;gap:8px;margin:5px 0;font-family:system-ui,sans-serif}}
  .row .n{{font-size:18px;color:var(--navy);font-weight:700;min-width:64px;text-align:right}}
  .row .bar{{height:16px;background:var(--navy);opacity:.88;border-radius:1px}}
  .row .bar.gold{{background:var(--gold)}}
  .row .lab{{font-size:14px;color:#444}}
  .row .lab small{{color:#aaa}}
  .cog{{border:1px solid var(--line);padding:10px 12px;margin:8px 0;background:#fff}}
  .cog .meaning{{font-size:15px;color:var(--navy);font-weight:700;margin-bottom:4px}}
  .cog .w{{display:inline-block;font-family:system-ui,sans-serif;font-size:13px;margin:2px 8px 2px 0;color:#333}}
  .cog .w b{{color:var(--gold)}}
  .note{{font-family:system-ui,sans-serif;font-size:12px;color:#8a8270;margin-top:6px}}
  footer{{margin-top:56px;padding-top:16px;border-top:1px solid var(--line);
    font-family:system-ui,sans-serif;font-size:12px;color:#8a8270}}
</style>
</head>
<body>
<header>
  <h1>多语词汇语料</h1>
  <div class="sub">英 · 西 · 法 · 粤为主体 · {total} 词条 · {nlang} 种语言 · 同源簇 {ncog} · DeepSeek 校正语言</div>
</header>

<h2>语言分布 · Language Distribution</h2>
{dist}

<h2>词性分布 · Part of Speech</h2>
{pos}

<h2>跨语言同源词 · Cognate Clusters</h2>
{cog}

<footer>个人多年手记词汇语料 · 语言标签经 DeepSeek 重判(四语 ~98%)· 低信心 {conf_low} 条 ·
仅四语(英西法粤)可信,详见 DIAGNOSIS.md</footer>
</body>
</html>"""


if __name__ == "__main__":
    main()
