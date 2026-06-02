# Polyglot Matrix

> 一份多年累积的个人多语词汇语料（英 / 西 / 法 / 粤为主），经 DeepSeek 重新校正语言标签后整理而成。

**在线**：https://beltran12138.github.io/POLYGLOT-MATRIX/

---

## 这是什么

14116 条手记词汇，每条含原文、词性与中文释义。原始数据的语言标签曾用字符集启发式判定，错误率约 50%（拉丁字母诸语互相误判）。本仓库用 DeepSeek 逐条重判语言，四语（英西法粤）准确率约 98%。

释义为多年亲手所记，是这份语料的真正价值——世上仅此一份。

## 真实语言分布（vocabulary_v4.json）

| 语言 | 数量 | 校正前 |
|---|---:|---:|
| English | 12262 | 12396 |
| Français | 863 | 10 |
| Español | 677 | 1295 |
| 粵語（带 jyutping） | 299 | 0 |
| 其余（荷/希腊/印尼，残值） | 14 | 0 |

法语从 10 → 863（原误标进西语桶），粤语从 0 → 299（原混在中文桶），西语去除英法污染。

## 仓库结构

```
vocabulary.json       原始数据（语言标签不可信，留作 raw 源）
vocabulary_v4.json    主数据：每条带 lang_new（校正语言）+ conf（信心）
index.html            可视化网页（语言分布 / 词性 / 跨语言同源词），Pages 入口

ep_relang.py          DeepSeek 语言重判脚本（生成 v4）
build_viz.py          生成 index.html
build_obsidian.py     导出 Obsidian 双链库（每词一 note，同源词互链）
build_anki.py         导出 Anki .apkg（按语言分子 deck，可选 TTS）

DIAGNOSIS.md          完整诊断与方法记录（含失败教训）
```

## 复现

```bash
# 语言重判需 DeepSeek key（写入 .env: DEEPSEEK_API_KEY=...）
python ep_relang.py --all          # vocabulary.json → vocabulary_v4.json

python build_viz.py                 # → index.html
python build_obsidian.py            # → obsidian_vault/
pip install genanki && python build_anki.py   # → polyglot_deck.apkg
```

`obsidian_vault/` 与 `.apkg` 为衍生物，不入库，由脚本本地重建。

## 已知局限（诚实说明）

- **无学习时序 / 集结构**：原始数据已被全局字母排序，原始记录顺序与"按集分语言"的结构不可逆丢失。详见 [DIAGNOSIS.md](DIAGNOSIS.md)。
- **罕见语言漏判**：EP 标题证明曾学过 9 语（含希腊、荷兰、阿拉伯、日语），但这些语言多以罗马转写记录、散落全表，被误判为英语。仅四语标签可信。
- 恢复完整 9 语结构需找回原始 `.txt` 笔记（已遗失）。

## License

MIT
