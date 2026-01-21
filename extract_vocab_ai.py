"""
🤖 AI-Powered Vocabulary Extractor
使用 Claude API 进行语义解析，替代传统正则表达式
"""

import json
import os
import glob
from anthropic import Anthropic

# ==========================================
# 🔧 配置区
# ==========================================
SOURCE_FOLDER = '.'
OUTPUT_FILE = 'vocabulary_enhanced.json'
API_KEY = os.getenv('ANTHROPIC_API_KEY')  # 从环境变量读取

client = Anthropic(api_key=API_KEY)

def parse_with_ai(text_line):
    """
    使用 Claude 进行智能解析
    返回结构化的词汇数据，包含自动补全的语言检测、词根词源等
    """
    if not text_line.strip():
        return None

    prompt = f"""你是一个专业的语言学家和词典编纂者。请分析以下语言学习笔记行，提取完整的词汇信息。

输入文本：{text_line}

请严格按照以下 JSON Schema 返回数据：
{{
    "word": "原始单词",
    "language": "ISO 639-1 语言代码 (en/es/fr/ja/zh 等)",
    "pos": "词性缩写 (n./v./adj./adv./prep. 等)",
    "definition": "中文释义（多个义项用 & 分隔）",
    "etymology": "词根词源（可选，如果能推断）",
    "example": "例句（可选，英文或原语言）",
    "synonyms": ["同义词列表（可选）"],
    "difficulty": "难度等级 1-5 (1=基础, 5=高级)"
}}

注意事项：
- 如果输入格式不规范，尽量智能推断
- 语言识别要准确（如 abogado=西班牙语, abimer=法语, abide=英语）
- 如果无法确定某字段，填 null
- 只返回 JSON，不要任何额外文字"""

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=512,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        # 解析 AI 返回的 JSON
        result_text = response.content[0].text.strip()
        # 去掉可能的 markdown 代码块标记
        if result_text.startswith('```'):
            result_text = result_text.split('\n', 1)[1].rsplit('\n', 1)[0]

        data = json.loads(result_text)

        # 兼容旧格式的字段映射
        return {
            "word": data.get("word", ""),
            "lang": data.get("language", "unknown"),
            "type": data.get("pos", "N/A"),
            "def": data.get("definition", ""),
            "etymology": data.get("etymology"),
            "example": data.get("example"),
            "synonyms": data.get("synonyms", []),
            "difficulty": data.get("difficulty", 3)
        }

    except Exception as e:
        print(f"   ⚠️ AI 解析失败: {text_line[:30]}... | 错误: {e}")
        # 降级方案：使用原始 Regex 逻辑
        return parse_line_fallback(text_line)

def parse_line_fallback(line):
    """降级方案：保留原有的正则表达式逻辑"""
    import re
    line = line.strip()
    if not line:
        return None

    pattern = r"^(\S+)\s+([^.]+?)\.(.*)$"
    match = re.match(pattern, line)

    if match:
        return {
            "word": match.group(1),
            "lang": "unknown",
            "type": match.group(2) + ".",
            "def": match.group(3).strip(),
            "etymology": None,
            "example": None,
            "synonyms": [],
            "difficulty": 3
        }
    return None

def main():
    if not API_KEY:
        print("❌ 请设置环境变量 ANTHROPIC_API_KEY")
        return

    all_vocab = []
    txt_files = glob.glob(os.path.join(SOURCE_FOLDER, '*.txt'))

    print(f"📂 发现 {len(txt_files)} 个文本文件...")
    print(f"🤖 使用 Claude AI 进行智能解析...\n")

    for file_path in txt_files:
        print(f"   -> 正在处理: {os.path.basename(file_path)}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for idx, line in enumerate(f, 1):
                    result = parse_with_ai(line)
                    if result:
                        all_vocab.append(result)
                        # 显示进度
                        if idx % 10 == 0:
                            print(f"      已处理 {idx} 行...")
        except Exception as e:
            print(f"   ⚠️ 读取文件出错: {e}")

    # 保存增强版 JSON
    print(f"\n💾 正在保存 {len(all_vocab)} 个单词到 {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_vocab, f, ensure_ascii=False, indent=2)

    print("✅ AI 增强处理完成！")
    print(f"📊 数据质量提升：")
    print(f"   - 精准语言识别")
    print(f"   - 自动词源补全")
    print(f"   - 难度评级")

if __name__ == "__main__":
    main()
