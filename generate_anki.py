"""
🎴 Anki Card Generator with TTS
自动生成 Anki 卡片包，包含原声发音
"""

import json
import random
import genanki
import edge_tts
import asyncio
import os
from pathlib import Path

# ==========================================
# 🔧 配置区
# ==========================================
VOCAB_FILE = 'vocabulary.json'
OUTPUT_DECK = 'polyglot_deck.apkg'
AUDIO_DIR = Path('./anki_audio')
AUDIO_DIR.mkdir(exist_ok=True)

# 语言 -> TTS 语音映射
VOICE_MAP = {
    'en': 'en-US-AriaNeural',
    'es': 'es-ES-ElviraNeural',
    'fr': 'fr-FR-DeniseNeural',
    'ja': 'ja-JP-NanamiNeural',
    'zh': 'zh-CN-XiaoxiaoNeural'
}

# Anki Model (卡片模板)
model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    'Polyglot Card',
    fields=[
        {'name': 'Word'},
        {'name': 'Language'},
        {'name': 'POS'},
        {'name': 'Definition'},
        {'name': 'Audio'},
        {'name': 'Example'},
        {'name': 'Etymology'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '''
                <div style="font-family: 'Space Grotesk', sans-serif; text-align: center; background: linear-gradient(135deg, #667eea, #764ba2); padding: 40px; border-radius: 20px;">
                    <div style="font-size: 48px; font-weight: bold; color: white; margin-bottom: 10px;">
                        {{Word}}
                    </div>
                    <div style="font-size: 18px; color: rgba(255,255,255,0.8);">
                        {{Language}} · {{POS}}
                    </div>
                    <div style="margin-top: 20px;">
                        {{Audio}}
                    </div>
                </div>
            ''',
            'afmt': '''
                {{FrontSide}}
                <hr style="border: 1px solid rgba(255,255,255,0.2); margin: 30px 0;">
                <div style="font-family: 'Noto Sans SC', sans-serif; padding: 20px; background: rgba(0,0,0,0.3); border-radius: 15px;">
                    <div style="font-size: 24px; color: #fff; margin-bottom: 15px;">
                        📖 {{Definition}}
                    </div>
                    {{#Example}}
                    <div style="font-size: 16px; color: rgba(255,255,255,0.7); font-style: italic; margin-top: 10px;">
                        💡 {{Example}}
                    </div>
                    {{/Example}}
                    {{#Etymology}}
                    <div style="font-size: 14px; color: rgba(255,255,255,0.5); margin-top: 10px;">
                        🌱 {{Etymology}}
                    </div>
                    {{/Etymology}}
                </div>
            ''',
        },
    ],
    css='''
        .card {
            font-family: 'Space Grotesk', sans-serif;
            background: #0a0a0a;
            color: white;
        }
    '''
)

async def generate_audio(word, lang, output_path):
    """使用 Edge TTS 生成发音"""
    voice = VOICE_MAP.get(lang, 'en-US-AriaNeural')
    try:
        communicate = edge_tts.Communicate(word, voice)
        await communicate.save(str(output_path))
        return True
    except Exception as e:
        print(f"   ⚠️ 生成发音失败 ({word}): {e}")
        return False

async def main():
    # 加载词汇数据
    print("📚 加载词汇数据...")
    with open(VOCAB_FILE, 'r', encoding='utf-8') as f:
        vocab_data = json.load(f)

    # 创建 Anki Deck
    deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31),
        'Polyglot Matrix Vocabulary'
    )

    media_files = []

    print(f"🎴 正在生成 {len(vocab_data)} 张卡片...\n")

    for idx, item in enumerate(vocab_data, 1):
        word = item['word']
        lang = item.get('lang', 'unknown')

        # 智能语言识别（与 dashboard 逻辑一致）
        if lang in ['Mixed', 'Unknown', 'unknown']:
            if word.isascii():
                lang = 'es' if item.get('type') in ['tr.', 'intr.'] else 'en'
            elif any('\u3040' <= c <= '\u30ff' for c in word):
                lang = 'ja'
            elif any('\u4e00' <= c <= '\u9fff' for c in word):
                lang = 'zh'

        # 生成音频文件
        audio_filename = f"{word.replace(' ', '_')}_{lang}.mp3"
        audio_path = AUDIO_DIR / audio_filename

        audio_field = ''
        if lang in VOICE_MAP and not audio_path.exists():
            print(f"   🔊 [{idx}/{len(vocab_data)}] 生成发音: {word} ({lang})")
            success = await generate_audio(word, lang, audio_path)
            if success:
                audio_field = f'[sound:{audio_filename}]'
                media_files.append(str(audio_path))
        elif audio_path.exists():
            audio_field = f'[sound:{audio_filename}]'
            media_files.append(str(audio_path))

        # 创建卡片
        note = genanki.Note(
            model=model,
            fields=[
                word,
                lang.upper(),
                item.get('type', 'N/A'),
                item.get('def', ''),
                audio_field,
                item.get('example', ''),
                item.get('etymology', '')
            ]
        )
        deck.add_note(note)

    # 打包为 .apkg
    print(f"\n📦 正在打包 Anki 卡片包...")
    package = genanki.Package(deck)
    package.media_files = media_files
    package.write_to_file(OUTPUT_DECK)

    print(f"✅ 完成！已生成: {OUTPUT_DECK}")
    print(f"📊 统计: {len(vocab_data)} 张卡片, {len(media_files)} 个音频文件")
    print(f"\n导入方法：打开 Anki -> 文件 -> 导入 -> 选择 {OUTPUT_DECK}")

if __name__ == "__main__":
    # 安装依赖提示
    try:
        import genanki
        import edge_tts
    except ImportError:
        print("❌ 缺少依赖库，请先安装：")
        print("   pip install genanki edge-tts")
        exit(1)

    asyncio.run(main())
