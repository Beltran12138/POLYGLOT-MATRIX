# -*- coding: utf-8 -*-
"""
步骤C-A · Anki 九语卡组生成器(重写,取代 generate_anki.py)
读 vocabulary_v4.json(真实 lang_new)→ 按语言分子 deck → navy/金/白 样式。
默认免音频(14116 条 TTS 联网逐条太慢易断;加 --audio 才生成,且建议配 --lang 限定单语言)。
用法:
  python build_anki.py                  # 全九语,无音频
  python build_anki.py --lang yue --audio  # 仅粤语 + TTS
依赖: genanki(必需) edge-tts(仅 --audio)
"""
import json, random, sys, asyncio
from pathlib import Path

SRC = "vocabulary_v4.json"
OUT = "polyglot_deck.apkg"
AUDIO_DIR = Path("./anki_audio")

LANG_NAME = {
    "en": "English", "es": "Español", "fr": "Français", "yue": "粵語",
    "el": "Ελληνικά", "nl": "Nederlands", "id": "Bahasa", "ja": "日本語",
    "ar": "العربية", "zh": "中文",
}
# 九语 edge-TTS 语音(粤语 zh-HK)
VOICE_MAP = {
    "en": "en-US-AriaNeural", "es": "es-ES-ElviraNeural", "fr": "fr-FR-DeniseNeural",
    "yue": "zh-HK-HiuMaanNeural", "el": "el-GR-AthinaNeural", "nl": "nl-NL-ColetteNeural",
    "id": "id-ID-GadisNeural", "ja": "ja-JP-NanamiNeural", "ar": "ar-SA-ZariyahNeural",
    "zh": "zh-CN-XiaoxiaoNeural",
}

CARD_CSS = """
.card{font-family:Georgia,"Songti SC",serif;background:#fbfaf7;color:#1a1a1a}
.head{background:#1B2A5A;color:#fff;padding:34px;text-align:center}
.word{font-size:42px;font-weight:700;letter-spacing:-.5px}
.meta{font-family:system-ui,sans-serif;font-size:14px;color:#C9A24C;margin-top:8px;text-transform:uppercase;letter-spacing:1px}
.back{padding:24px;font-size:20px;border-top:3px solid #C9A24C}
.ep{font-family:system-ui,sans-serif;font-size:12px;color:#8a8270}
"""


def build_model():
    return __import__("genanki").Model(
        random.randrange(1 << 30, 1 << 31), "Polyglot Card v3",
        fields=[{"name": "Word"}, {"name": "Lang"}, {"name": "POS"},
                {"name": "Def"}, {"name": "Audio"}],
        templates=[{
            "name": "Card 1",
            "qfmt": '<div class="head"><div class="word">{{Word}}</div>'
                    '<div class="meta">{{Lang}} · {{POS}}</div>{{Audio}}</div>',
            "afmt": '{{FrontSide}}<div class="back">{{Def}}</div>',
        }], css=CARD_CSS)


async def gen_audio(genanki, deck, model, items, media):
    import edge_tts
    for i, x in enumerate(items, 1):
        L = x["lang_new"]
        fn = f"{x['word'].replace(' ','_')}_{L}.mp3"
        p = AUDIO_DIR / fn
        af = ""
        if L in VOICE_MAP:
            if not p.exists():
                try:
                    await edge_tts.Communicate(x["word"], VOICE_MAP[L]).save(str(p))
                except Exception as e:
                    print(f"  TTS fail {x['word']}: {e}"); p = None
            if p and p.exists():
                af = f"[sound:{fn}]"; media.append(str(p))
        if i % 200 == 0:
            print(f"  audio {i}/{len(items)}")
        add_note(genanki, deck, model, x, af)


def add_note(genanki, deck, model, x, audio=""):
    deck.add_note(genanki.Note(model=model, fields=[
        x["word"], LANG_NAME.get(x["lang_new"], x["lang_new"]),
        x.get("type", ""), x.get("def", ""), audio,
    ]))


def main():
    genanki = __import__("genanki")
    want_lang = sys.argv[sys.argv.index("--lang") + 1] if "--lang" in sys.argv else None
    want_audio = "--audio" in sys.argv

    d = [x for x in json.load(open(SRC, encoding="utf-8")) if x.get("lang_new")]
    if want_lang:
        d = [x for x in d if x["lang_new"] == want_lang]

    model = build_model()
    # 顶层 deck + 每语言子 deck(Anki 用 :: 表层级)
    decks = {}
    import collections
    by_lang = collections.defaultdict(list)
    for x in d:
        by_lang[x["lang_new"]].append(x)

    media = []
    if want_audio:
        AUDIO_DIR.mkdir(exist_ok=True)
        # 音频模式:逐语言异步
        all_decks = []
        for L, items in by_lang.items():
            dk = genanki.Deck(random.randrange(1 << 30, 1 << 31),
                              f"Polyglot Matrix::{LANG_NAME.get(L,L)}")
            asyncio.run(gen_audio(genanki, dk, model, items, media))
            all_decks.append(dk)
        pkg = genanki.Package(all_decks); pkg.media_files = media
    else:
        all_decks = []
        for L, items in by_lang.items():
            dk = genanki.Deck(random.randrange(1 << 30, 1 << 31),
                              f"Polyglot Matrix::{LANG_NAME.get(L,L)}")
            for x in items:
                add_note(genanki, dk, model, x)
            all_decks.append(dk)
        pkg = genanki.Package(all_decks)

    pkg.write_to_file(OUT)
    print(f"写出 {OUT}  {len(d)} 卡  {len(by_lang)} 语言子组  音频 {len(media)}")
    print("  ", {LANG_NAME.get(k,k): len(v) for k, v in by_lang.items()})


if __name__ == "__main__":
    try:
        import genanki  # noqa
    except ImportError:
        print("缺 genanki: pip install genanki"); sys.exit(1)
    main()
