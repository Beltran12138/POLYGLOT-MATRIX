import re
import json
import os
import glob

# ==========================================
# 🔧 配置区
# ==========================================
# 你的文本文件所在的文件夹路径 ('.' 表示当前文件夹)
SOURCE_FOLDER = '.'
# 输出的文件名
OUTPUT_FILE = 'vocabulary.json'

def parse_line(line):
    """
    解析单行文本，提取 单词、词性、释义
    支持格式: "单词 词性.释义" (例如: ablandar tr.使变软)
    """
    line = line.strip()
    if not line:
        return None

    # -------------------------------------------------------
    # 核心正则表达式 (Regex Magic)
    # ^(\S+)    -> 捕获组1(单词): 行首的非空白字符
    # \s+       -> 间隔: 一个或多个空格/Tab
    # ([^.]+?)  -> 捕获组2(词性): 非点的字符 (非贪婪匹配)
    # \.        -> 分隔符: 必须有一个点
    # (.*)$     -> 捕获组3(释义): 点后面的所有内容
    # -------------------------------------------------------
    pattern = r"^(\S+)\s+([^.]+?)\.(.*)$"
    
    match = re.match(pattern, line)
    
    if match:
        word = match.group(1)
        pos = match.group(2)  # Part of Speech (词性)
        definition = match.group(3)
        
        # 简单的语言推测逻辑 (可选，根据你的文件名或特定字符优化)
        # 这里默认设为 "Mixed"，你可以后续在 JSON 里批量修改
        lang = "Mixed" 
        if any("\u3040" <= c <= "\u309f" or "\u30a0" <= c <= "\u30ff" for c in word):
            lang = "Japanese" # 如果单词包含平假名/片假名

        return {
            "word": word,
            "lang": lang, 
            "type": pos + ".", # 补回那个点，看起来更习惯
            "def": definition.strip()
        }
    else:
        # 容错处理：如果格式不是 "词性.释义"，尝试简单的 "单词 释义" 分割
        # 比如日记里的: "ア=a=あ" 这种格式
        parts = line.split(maxsplit=1)
        if len(parts) == 2:
            return {
                "word": parts[0],
                "lang": "Unknown",
                "type": "N/A",
                "def": parts[1].strip()
            }
        return None

def main():
    all_vocab = []
    # 查找所有 .txt 文件
    txt_files = glob.glob(os.path.join(SOURCE_FOLDER, '*.txt'))
    
    print(f"📂 发现 {len(txt_files)} 个文本文件...")

    for file_path in txt_files:
        print(f"   -> 正在处理: {os.path.basename(file_path)}")
        try:
            # 使用 utf-8 编码读取 (如果报错，可以尝试 'gbk')
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    result = parse_line(line)
                    if result:
                        all_vocab.append(result)
        except Exception as e:
            print(f"   ⚠️ 读取文件出错: {e}")

    # 保存为 JSON
    print(f"💾 正在保存 {len(all_vocab)} 个单词到 {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_vocab, f, ensure_ascii=False, indent=4)
    
    print("✅ 完成！你可以直接复制 vocabulary.json 的内容到你的网页代码里了。")

if __name__ == "__main__":
    main()