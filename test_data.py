# -*- coding: utf-8 -*-
"""
测试数据完整性和功能模块
"""

import json
import sys

def test_vocabulary_json():
    """测试 vocabulary.json 数据加载"""
    print("=" * 60)
    print("📊 测试 vocabulary.json 数据加载")
    print("=" * 60)

    try:
        with open('vocabulary.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"✅ 数据加载成功")
        print(f"📈 总词汇量: {len(data)} 个单词\n")

        # 语言分布统计
        lang_dist = {}
        pos_dist = {}

        for item in data:
            lang = item.get('lang', 'Unknown')
            pos = item.get('type', 'N/A')

            lang_dist[lang] = lang_dist.get(lang, 0) + 1
            pos_dist[pos] = pos_dist.get(pos, 0) + 1

        print("🌍 语言分布:")
        for lang, count in sorted(lang_dist.items(), key=lambda x: -x[1])[:10]:
            print(f"   {lang:15s}: {count:5d} 个")

        print(f"\n🏷️  词性分布 (Top 10):")
        for pos, count in sorted(pos_dist.items(), key=lambda x: -x[1])[:10]:
            print(f"   {pos:15s}: {count:5d} 个")

        print(f"\n📝 示例数据 (前3个):")
        for i, item in enumerate(data[:3], 1):
            print(f"\n   [{i}] {item['word']}")
            print(f"       语言: {item.get('lang', 'N/A')}")
            print(f"       词性: {item.get('type', 'N/A')}")
            print(f"       释义: {item.get('def', 'N/A')[:50]}...")

        return True

    except Exception as e:
        print(f"❌ 数据加载失败: {e}")
        return False

def test_html_files():
    """测试 HTML 文件存在性"""
    print("\n" + "=" * 60)
    print("🌐 测试 HTML 文件")
    print("=" * 60)

    files = {
        'index.html': '原始展示页面',
        'dashboard.html': '数据分析仪表盘',
        'semantic_search.html': '语义搜索引擎'
    }

    import os
    for file, desc in files.items():
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"✅ {file:25s} - {desc} ({size:,} bytes)")
        else:
            print(f"❌ {file:25s} - 文件不存在")

def test_python_scripts():
    """测试 Python 脚本存在性"""
    print("\n" + "=" * 60)
    print("🐍 测试 Python 脚本")
    print("=" * 60)

    scripts = {
        'extract_vocab.py': '原始正则解析器',
        'extract_vocab_ai.py': 'AI 增强解析器',
        'generate_anki.py': 'Anki 卡片生成器',
        'word_poster_generator.py': '海报生成器'
    }

    import os
    for script, desc in scripts.items():
        if os.path.exists(script):
            print(f"✅ {script:30s} - {desc}")
        else:
            print(f"❌ {script:30s} - 文件不存在")

def main():
    print("\n🚀 Polyglot Matrix - 模块测试报告\n")

    # 测试数据
    data_ok = test_vocabulary_json()

    # 测试文件
    test_html_files()
    test_python_scripts()

    print("\n" + "=" * 60)
    if data_ok:
        print("✅ 所有核心模块测试通过！")
        print("\n📌 下一步:")
        print("   1. 在浏览器中打开 dashboard.html 查看数据可视化")
        print("   2. 打开 semantic_search.html 测试语义搜索")
        print("   3. 运行 generate_anki.py 生成 Anki 卡片")
    else:
        print("⚠️  部分测试失败，请检查数据文件")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    # 设置 UTF-8 输出
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

    main()
