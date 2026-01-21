# -*- coding: utf-8 -*-
"""
⚡ 快速添加单词工具
交互式命令行界面，快速添加单词到词库
"""

import json
import sys
from pathlib import Path

def quick_add_word():
    """交互式添加单词"""
    print("\n" + "=" * 60)
    print("⚡ Quick Add - 快速添加单词")
    print("=" * 60)
    print("💡 提示: 输入 'q' 或 'quit' 退出\n")

    vocab_file = 'vocabulary.json'

    # 读取现有数据
    try:
        with open(vocab_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
        print("⚠️  vocabulary.json 不存在，将创建新文件\n")

    added_count = 0

    while True:
        # 输入单词
        word = input("📝 单词 (word): ").strip()
        if word.lower() in ['q', 'quit', '']:
            break

        # 输入语言
        print("   语言选项: en (英语), es (西班牙语), fr (法语), ja (日语), zh (中文)")
        lang = input("🌍 语言 (lang): ").strip().lower() or 'en'

        # 输入词性
        print("   常见词性: n. (名词), v. (动词), adj. (形容词), adv. (副词)")
        pos = input("🏷️  词性 (type): ").strip() or 'n.'
        if not pos.endswith('.'):
            pos += '.'

        # 输入释义
        definition = input("📖 释义 (def): ").strip()

        # 可选：例句
        example = input("💡 例句 (可选，直接回车跳过): ").strip() or None

        # 可选：词源
        etymology = input("🌱 词源 (可选，直接回车跳过): ").strip() or None

        # 创建词条
        entry = {
            "word": word,
            "lang": lang,
            "type": pos,
            "def": definition
        }

        if example:
            entry["example"] = example
        if etymology:
            entry["etymology"] = etymology

        # 检查重复
        existing = [v for v in data if v['word'].lower() == word.lower() and v.get('lang') == lang]
        if existing:
            print(f"\n⚠️  单词 '{word}' ({lang}) 已存在")
            overwrite = input("   是否覆盖? (y/n): ").strip().lower()
            if overwrite == 'y':
                # 删除旧条目
                data = [v for v in data if not (v['word'].lower() == word.lower() and v.get('lang') == lang)]
                data.append(entry)
                print("✅ 已更新")
                added_count += 1
            else:
                print("❌ 已跳过")
        else:
            data.append(entry)
            print("✅ 已添加")
            added_count += 1

        # 继续添加?
        continue_add = input("\n➕ 继续添加? (Enter 继续 / n 退出): ").strip().lower()
        if continue_add == 'n':
            break

        print()  # 空行分隔

    # 保存数据
    if added_count > 0:
        # 备份
        backup_file = vocab_file.replace('.json', '_backup.json')
        if Path(vocab_file).exists():
            with open(backup_file, 'w', encoding='utf-8') as f:
                with open(vocab_file, 'r', encoding='utf-8') as orig:
                    f.write(orig.read())

        # 保存
        with open(vocab_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print("\n" + "=" * 60)
        print(f"✅ 已成功添加 {added_count} 个单词到 {vocab_file}")
        print(f"📊 当前总词汇量: {len(data)} 个")
        print("=" * 60)

        print("\n💡 下一步:")
        print("   1. 刷新 dashboard.html 查看更新")
        print("   2. 运行 test_data.py 验证数据")
        print("   3. 提交到 Git: git add . && git commit -m 'Add words via quick_add'")
    else:
        print("\n⚠️  没有添加任何单词")

def main():
    try:
        quick_add_word()
    except KeyboardInterrupt:
        print("\n\n👋 已取消")
        sys.exit(0)

if __name__ == "__main__":
    # 设置 UTF-8 输出
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

    main()
