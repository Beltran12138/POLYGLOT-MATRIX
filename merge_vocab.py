# -*- coding: utf-8 -*-
"""
📦 词汇合并工具
将新单词合并到主数据库，自动去重
"""

import json
import sys
from pathlib import Path

def merge_vocabularies(main_file, new_files):
    """
    合并多个词汇文件到主数据库

    Args:
        main_file: 主数据库文件路径
        new_files: 新词汇文件列表
    """
    print("=" * 60)
    print("📦 Vocabulary Merger")
    print("=" * 60)

    # 读取主数据库
    try:
        with open(main_file, 'r', encoding='utf-8') as f:
            main_data = json.load(f)
        print(f"✅ 主数据库: {len(main_data)} 个单词")
    except FileNotFoundError:
        main_data = []
        print("⚠️  主数据库不存在，将创建新文件")

    # 读取所有新文件
    all_new_words = []
    for new_file in new_files:
        try:
            with open(new_file, 'r', encoding='utf-8') as f:
                new_data = json.load(f)
            all_new_words.extend(new_data)
            print(f"✅ {new_file}: {len(new_data)} 个单词")
        except FileNotFoundError:
            print(f"❌ 文件不存在: {new_file}")
        except json.JSONDecodeError:
            print(f"❌ JSON 格式错误: {new_file}")

    if not all_new_words:
        print("\n⚠️  没有找到新单词")
        return

    print(f"\n📊 合并前统计:")
    print(f"   主数据库: {len(main_data)} 个")
    print(f"   新单词:   {len(all_new_words)} 个")

    # 合并数据
    combined = main_data + all_new_words

    # 去重（基于单词 + 语言）
    seen = set()
    unique_words = []
    duplicates = 0

    for item in combined:
        word = item.get('word', '').lower()
        lang = item.get('lang', 'unknown')
        key = f"{word}_{lang}"

        if key not in seen:
            seen.add(key)
            unique_words.append(item)
        else:
            duplicates += 1

    print(f"\n🔍 去重统计:")
    print(f"   发现重复: {duplicates} 个")
    print(f"   唯一单词: {len(unique_words)} 个")

    # 备份原文件
    if Path(main_file).exists():
        backup_file = main_file.replace('.json', '_backup.json')
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(main_data, f, ensure_ascii=False, indent=2)
        print(f"\n💾 原数据已备份到: {backup_file}")

    # 保存合并后的数据
    with open(main_file, 'w', encoding='utf-8') as f:
        json.dump(unique_words, f, ensure_ascii=False, indent=2)

    print(f"💾 合并数据已保存到: {main_file}")

    # 统计新增单词
    new_count = len(unique_words) - len(main_data)
    print(f"\n✅ 合并完成！")
    print(f"   新增单词: {new_count} 个")
    print(f"   总词汇量: {len(unique_words)} 个")

def main():
    if len(sys.argv) < 2:
        print("📖 使用方法:")
        print("   python merge_vocab.py <新词汇文件1> [新词汇文件2] ...")
        print("\n📝 示例:")
        print("   python merge_vocab.py new_words.json")
        print("   python merge_vocab.py file1.json file2.json file3.json")
        sys.exit(1)

    main_file = 'vocabulary.json'
    new_files = sys.argv[1:]

    merge_vocabularies(main_file, new_files)

    print("\n💡 下一步:")
    print("   1. 运行 test_data.py 验证数据")
    print("   2. 刷新 dashboard.html 查看更新")
    print("   3. 提交到 Git: git add vocabulary.json && git commit -m 'Add new words'")

if __name__ == "__main__":
    # 设置 UTF-8 输出
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

    main()
