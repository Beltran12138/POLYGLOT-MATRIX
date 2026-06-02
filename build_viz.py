# -*- coding: utf-8 -*-
"""
步骤C-B · 学习史可视化网页生成器
读 vocabulary_v4.json → 聚合(语言分布 / EP×语言扩张矩阵 / 同源词簇) → 单 HTML。
样式:navy #1B2A5A + 金 #C9A24C + 白,editorial 风,反 AI slop(无渐变/无均质方块网格)。
用法: python build_viz.py   →  写出 polyglot_viz.html
"""
import json, collections, html

SRC = "vocabulary_v4.json"
OUT = "polyglot_viz.html"

LANG_NAME = {
    "en": "English", "es": "Español", "fr": "Français", "yue": "粵語",
    "el": "Ελληνικά", "nl": "Nederlands", "id": "Bahasa", "ja": "日本語",
    "ar": "العربية", "zh": "中文",
}


def norm_def(s):
    """归一化释义取首义,用于跨语言同源/同义聚类。"""
    return s.split("&")[0].split("/")[0].strip()


def main():
    d = json.load(open(SRC, encoding="utf-8"))
    d = [x for x in d if x.get("lang_new")]
    N = len(d)

    # 1) 语言分布
    dist = collections.Counter(x["lang_new"] for x in d)

    # 2) 词性分布(EP 切分已证无效,改用有效维度:词性)
    pos = collections.Counter()
    for x in d:
        t = x.get("type", "").strip().rstrip(".").split("/")[0].split("&")[0].strip()
        if t and len(t) <= 6:
            pos[t] += 1

    # 3) 同源/同义簇:同一首义释义,跨 >=2 语言
    by_def = collections.defaultdict(list)
    for x in d:
        nd = norm_def(x["def"])
        if nd and len(nd) <= 8:  # 短义更可能真同义
            by_def[nd].append((x["lang_new"], x["word"]))
    cognates = []
    for nd, items in by_def.items():
        langs = {l for l, w in items}
        if len(langs) >= 3:  # 至少 3 语共享 → 强同源候选
            cognates.append((nd, sorted(set(items))))
    cognates.sort(key=lambda t: -len({l for l, w in t[1]}))

    # 4) 信心
    conf_low = sum(1 for x in d if x.get("conf", 1) < 0.6)

    # ---- 组装前端数据 ----
    langs_order = [l for l, _ in dist.most_common()]
    data = {
        "total": N,
        "dist": [{"lang": LANG_NAME.get(l, l), "iso": l, "n": dist[l]} for l in langs_order],
        "pos": [{"t": t, "n": n} for t, n in pos.most_common(12)],
        "cognates": [
            {"def": nd, "words": [{"iso": l, "lang": LANG_NAME.get(l, l), "word": w} for l, w in items]}
            for nd, items in cognates[:40]
        ],
        "conf_low": conf_low,
        "langnames": LANG_NAME,
    }
    blob = json.dumps(data, ensure_ascii=False)

    html_doc = HTML_TMPL.replace("/*DATA*/", blob)
    open(OUT, "w", encoding="utf-8").write(html_doc)
    print(f"写出 {OUT}")
    print(f"  总 {N} 条  语言 {len(dist)} 种  同源簇 {len(cognates)} 个  低信心 {conf_low}")
    print("  语言分布:", {LANG_NAME.get(l, l): dist[l] for l in langs_order})


HTML_TMPL = r"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Polyglot Matrix · 九语学习史</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<style>
  :root{--navy:#1B2A5A;--gold:#C9A24C;--ink:#1a1a1a;--paper:#fbfaf7;--line:#e3ddd0;}
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:var(--paper);color:var(--ink);font-family:"Georgia","Songti SC",serif;line-height:1.5;padding:48px 24px;max-width:1080px;margin:0 auto}
  header{border-bottom:3px solid var(--navy);padding-bottom:16px;margin-bottom:8px}
  h1{font-size:34px;color:var(--navy);letter-spacing:-.5px;font-weight:700}
  .sub{color:#6b6453;font-size:14px;margin-top:6px;font-family:system-ui,sans-serif}
  h2{font-size:13px;letter-spacing:2px;text-transform:uppercase;color:var(--gold);
     font-family:system-ui,sans-serif;font-weight:700;margin:44px 0 14px;border-left:4px solid var(--gold);padding-left:10px}
  .grid{display:grid;grid-template-columns:1fr 1fr;gap:32px}
  .stat{display:flex;align-items:baseline;gap:8px;margin:4px 0;font-family:system-ui,sans-serif}
  .stat .n{font-size:22px;color:var(--navy);font-weight:700;min-width:64px;text-align:right}
  .stat .bar{height:14px;background:var(--navy);opacity:.85}
  .stat .lab{font-size:14px;color:#444}
  .cog{border:1px solid var(--line);padding:10px 12px;margin:8px 0;background:#fff}
  .cog .meaning{font-size:15px;color:var(--navy);font-weight:700;margin-bottom:4px}
  .cog .w{display:inline-block;font-family:system-ui,sans-serif;font-size:13px;margin:2px 8px 2px 0;color:#333}
  .cog .w b{color:var(--gold)}
  .note{font-family:system-ui,sans-serif;font-size:12px;color:#8a8270;margin-top:6px}
  canvas{background:#fff;border:1px solid var(--line);padding:8px}
  @media(max-width:760px){.grid{grid-template-columns:1fr}}
</style>
</head>
<body>
<header>
  <h1>九语学习史</h1>
  <div class="sub" id="sub"></div>
</header>

<h2>语言分布 · Language Distribution</h2>
<div id="dist"></div>

<h2>词性分布 · Part of Speech</h2>
<canvas id="pos" height="110"></canvas>
<div class="note">名/动/形/副等词性占比。</div>

<h2>跨语言同源词 · Cognate Clusters</h2>
<div id="cog"></div>

<script>
const D = /*DATA*/;
document.getElementById('sub').textContent =
  D.total.toLocaleString()+' 词条 · '+D.dist.length+' 种语言 · '+D.eps.length+' 集 · 低信心 '+D.conf_low;

// 分布条
const max = D.dist[0].n;
document.getElementById('dist').innerHTML = D.dist.map(r=>
  `<div class="stat"><span class="n">${r.n.toLocaleString()}</span>`+
  `<span class="bar" style="width:${Math.max(2,r.n/max*420)}px"></span>`+
  `<span class="lab">${r.lang} <small style="color:#aaa">(${r.iso})</small></span></div>`
).join('');

// 词性分布(横向条)
new Chart(document.getElementById('pos'),{
  type:'bar',
  data:{labels:D.pos.map(p=>p.t),
    datasets:[{data:D.pos.map(p=>p.n),backgroundColor:'#1B2A5A',borderColor:'#C9A24C',borderWidth:1}]},
  options:{indexAxis:'y',responsive:true,plugins:{legend:{display:false}},
    scales:{x:{grid:{color:'#eee'}},y:{grid:{display:false},ticks:{font:{family:'system-ui',size:11}}}}}
});

// 同源词
document.getElementById('cog').innerHTML = D.cognates.map(c=>
  `<div class="cog"><div class="meaning">${c.def}</div>`+
  c.words.map(w=>`<span class="w"><b>${w.word}</b> ${w.lang}</span>`).join('')+
  `</div>`
).join('') || '<div class="note">无足够跨语言同义簇</div>';
</script>
</body>
</html>"""


if __name__ == "__main__":
    main()
