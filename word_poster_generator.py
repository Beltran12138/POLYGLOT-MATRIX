"""
📸 Word of the Day Poster Generator
自动生成 Instagram 风格的单词海报
"""

import json
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

# ==========================================
# 🔧 配置区
# ==========================================
VOCAB_FILE = 'vocabulary.json'
OUTPUT_DIR = Path('./word_posters')
OUTPUT_DIR.mkdir(exist_ok=True)

# 画布尺寸 (Instagram Post: 1080x1080)
WIDTH, HEIGHT = 1080, 1080

# 语言主题色
THEME_COLORS = {
    'en': {
        'bg': [(102, 126, 234), (118, 75, 162)],  # 紫蓝渐变
        'accent': '#667eea',
        'name': 'English'
    },
    'es': {
        'bg': [(240, 147, 251), (245, 87, 108)],  # 粉红渐变
        'accent': '#f093fb',
        'name': 'Español'
    },
    'fr': {
        'bg': [(79, 172, 254), (0, 242, 254)],  # 青蓝渐变
        'accent': '#4facfe',
        'name': 'Français'
    },
    'ja': {
        'bg': [(250, 112, 154), (254, 225, 64)],  # 樱花粉渐变
        'accent': '#fa709a',
        'name': '日本語'
    },
    'zh': {
        'bg': [(48, 207, 208), (51, 8, 103)],  # 青紫渐变
        'accent': '#30cfd0',
        'name': '中文'
    }
}

def create_gradient(draw, width, height, color1, color2):
    """创建渐变背景"""
    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b))

def add_noise_texture(image):
    """添加噪点质感"""
    noise = Image.new('RGBA', image.size)
    pixels = noise.load()
    for i in range(image.width):
        for j in range(image.height):
            if random.random() > 0.95:
                pixels[i, j] = (255, 255, 255, random.randint(10, 30))
    return Image.alpha_composite(image.convert('RGBA'), noise)

def generate_poster(word_data, output_path):
    """生成单词海报"""
    # 智能识别语言
    lang = word_data.get('lang', 'unknown')
    word = word_data['word']

    if lang in ['Mixed', 'Unknown', 'unknown']:
        if word.isascii():
            lang = 'es' if word_data.get('type') in ['tr.', 'intr.'] else 'en'
        elif any('\u3040' <= c <= '\u30ff' for c in word):
            lang = 'ja'
        elif any('\u4e00' <= c <= '\u9fff' for c in word):
            lang = 'zh'
        else:
            lang = 'en'

    theme = THEME_COLORS.get(lang, THEME_COLORS['en'])

    # 创建画布
    img = Image.new('RGB', (WIDTH, HEIGHT), 'white')
    draw = ImageDraw.Draw(img)

    # 渐变背景
    create_gradient(draw, WIDTH, HEIGHT, theme['bg'][0], theme['bg'][1])

    # 添加噪点
    img = add_noise_texture(img)
    draw = ImageDraw.Draw(img)

    # 加载字体（需要下载字体文件，这里使用默认）
    try:
        font_word = ImageFont.truetype('arial.ttf', 120)
        font_def = ImageFont.truetype('arial.ttf', 40)
        font_meta = ImageFont.truetype('arial.ttf', 30)
    except:
        font_word = ImageFont.load_default()
        font_def = ImageFont.load_default()
        font_meta = ImageFont.load_default()

    # 绘制主单词
    word_bbox = draw.textbbox((0, 0), word, font=font_word)
    word_width = word_bbox[2] - word_bbox[0]
    word_x = (WIDTH - word_width) // 2

    # 添加阴影效果
    draw.text((word_x + 4, 304), word, fill=(0, 0, 0, 128), font=font_word)
    draw.text((word_x, 300), word, fill='white', font=font_word)

    # 绘制词性和语言标签
    meta_text = f"{theme['name']} · {word_data.get('type', 'N/A')}"
    meta_bbox = draw.textbbox((0, 0), meta_text, font=font_meta)
    meta_width = meta_bbox[2] - meta_bbox[0]
    draw.text(((WIDTH - meta_width) // 2, 450), meta_text,
              fill=(255, 255, 255, 200), font=font_meta)

    # 绘制释义（分行处理）
    definition = word_data.get('def', '')
    max_chars = 30
    def_lines = []
    current_line = ''
    for char in definition:
        if char == '&':
            if current_line:
                def_lines.append(current_line.strip())
            current_line = ''
        else:
            current_line += char
            if len(current_line) >= max_chars:
                def_lines.append(current_line.strip())
                current_line = ''
    if current_line:
        def_lines.append(current_line.strip())

    y_offset = 550
    for line in def_lines[:3]:  # 最多显示3行
        line_bbox = draw.textbbox((0, 0), line, font=font_def)
        line_width = line_bbox[2] - line_bbox[0]
        draw.text(((WIDTH - line_width) // 2, y_offset), line,
                  fill='white', font=font_def)
        y_offset += 60

    # 底部装饰
    draw.rectangle([(0, HEIGHT - 100), (WIDTH, HEIGHT)],
                   fill=(0, 0, 0, 100))
    watermark = "📚 Polyglot Matrix"
    wm_bbox = draw.textbbox((0, 0), watermark, font=font_meta)
    wm_width = wm_bbox[2] - wm_bbox[0]
    draw.text(((WIDTH - wm_width) // 2, HEIGHT - 60), watermark,
              fill=(255, 255, 255, 180), font=font_meta)

    # 保存
    img.save(output_path, quality=95, optimize=True)
    print(f"✅ 已生成: {output_path.name}")

def main():
    # 加载词汇
    with open(VOCAB_FILE, 'r', encoding='utf-8') as f:
        vocab_data = json.load(f)

    print(f"📸 Word Poster Generator 启动...")
    print(f"📚 加载了 {len(vocab_data)} 个单词\n")

    # 选择模式
    print("请选择生成模式:")
    print("1. 生成单个随机单词海报")
    print("2. 批量生成前 10 个单词")
    print("3. 生成所有单词海报 (谨慎使用)")
    choice = input("输入选项 (1/2/3): ").strip()

    if choice == '1':
        word = random.choice(vocab_data)
        filename = f"{word['word'].replace(' ', '_')}_poster.png"
        generate_poster(word, OUTPUT_DIR / filename)
    elif choice == '2':
        for word in vocab_data[:10]:
            filename = f"{word['word'].replace(' ', '_')}_poster.png"
            generate_poster(word, OUTPUT_DIR / filename)
    elif choice == '3':
        confirm = input(f"⚠️  将生成 {len(vocab_data)} 张海报，确认吗? (yes/no): ")
        if confirm.lower() == 'yes':
            for idx, word in enumerate(vocab_data, 1):
                filename = f"{word['word'].replace(' ', '_')}_poster.png"
                generate_poster(word, OUTPUT_DIR / filename)
                if idx % 10 == 0:
                    print(f"   进度: {idx}/{len(vocab_data)}")

    print(f"\n🎉 完成！海报已保存到: {OUTPUT_DIR}")

if __name__ == "__main__":
    try:
        from PIL import Image, ImageDraw, ImageFont, ImageFilter
    except ImportError:
        print("❌ 缺少依赖库，请先安装：")
        print("   pip install Pillow")
        exit(1)

    main()
