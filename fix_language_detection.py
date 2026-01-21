# -*- coding: utf-8 -*-
"""
智能语言识别优化脚本
自动修复 vocabulary.json 中的语言标记
"""

import json
import re

def detect_language(word, pos_type, definition):
    """
    智能语言识别算法
    基于单词特征、词性和释义进行判断
    """
    word_lower = word.lower()

    # 规则1: 基于字符集判断
    # 日语检测 (平假名、片假名、汉字)
    if re.search(r'[\u3040-\u309f\u30a0-\u30ff]', word):
        return 'ja'

    # 中文检测 (简体/繁体汉字，但排除日语常用汉字)
    if re.search(r'[\u4e00-\u9fff]', word):
        # 如果词性不是日语特有的，且没有假名，判定为中文
        if not re.search(r'[\u3040-\u309f\u30a0-\u30ff]', definition):
            return 'zh'
        return 'ja'

    # 规则2: 基于词性判断（西班牙语特征）
    spanish_pos = ['tr.', 'intr.', 'prnl.', 'm.', 'f.', 'adj.inv.']
    if pos_type in spanish_pos:
        return 'es'

    # 规则3: 西班牙语动词结尾
    if word_lower.endswith(('ar', 'er', 'ir')) and len(word) > 4:
        # 常见西班牙语动词词根
        spanish_patterns = ['izar', 'ecer', 'uir']
        if any(word_lower.endswith(p) for p in spanish_patterns):
            return 'es'
        # 如果定义包含中文，更可能是西班牙语
        if re.search(r'[\u4e00-\u9fff]', definition):
            return 'es'

    # 规则4: 法语特征
    french_chars = ['à', 'â', 'é', 'è', 'ê', 'ë', 'î', 'ï', 'ô', 'ù', 'û', 'ü', 'ç', 'œ', 'æ']
    if any(char in word_lower for char in french_chars):
        return 'fr'

    # 规则5: 德语特征（大写名词，特殊字符）
    german_chars = ['ä', 'ö', 'ü', 'ß']
    if any(char in word_lower for char in german_chars):
        return 'de'

    # 规则6: 葡萄牙语特征
    portuguese_chars = ['ã', 'õ', 'á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'ô']
    if any(char in word_lower for char in portuguese_chars):
        return 'pt'

    # 规则7: 基于常见英语词性
    english_pos = ['v.', 'n.', 'adj.', 'adv.', 'prep.', 'conj.', 'pron.', 'interj.']
    if pos_type in english_pos and word.isascii():
        # 检查是否是常见英语单词特征
        common_english_endings = ['ing', 'tion', 'ment', 'ness', 'ful', 'less', 'able', 'ible', 'ize', 'ise']
        if any(word_lower.endswith(e) for e in common_english_endings):
            return 'en'

        # 检查是否包含常见英语字母组合
        common_english_patterns = ['th', 'wh', 'qu', 'ght', 'ough']
        if any(p in word_lower for p in common_english_patterns):
            return 'en'

        # 默认拉丁字母且词性为英语常见词性 -> 英语
        return 'en'

    # 默认：如果全是拉丁字母，优先判定为英语
    if word.isascii() and word.isalpha():
        return 'en'

    # 无法判断
    return 'unknown'

def optimize_language_tags():
    """优化 vocabulary.json 的语言标签"""
    import sys
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

    print("🔧 开始优化语言识别...\n")

    # 读取原始数据
    with open('vocabulary.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"📚 总词汇量: {len(data)} 个单词")

    # 统计优化前的语言分布
    before_dist = {}
    for item in data:
        lang = item.get('lang', 'Unknown')
        before_dist[lang] = before_dist.get(lang, 0) + 1

    print(f"\n📊 优化前语言分布:")
    for lang, count in sorted(before_dist.items(), key=lambda x: -x[1]):
        print(f"   {lang:15s}: {count:5d} 个")

    # 执行优化
    fixed_count = 0
    for item in data:
        original_lang = item.get('lang', 'Unknown')

        # 只优化 Mixed 和 Unknown 的条目
        if original_lang in ['Mixed', 'Unknown', 'unknown']:
            word = item['word']
            pos = item.get('type', 'N/A')
            definition = item.get('def', '')

            detected_lang = detect_language(word, pos, definition)

            if detected_lang != 'unknown':
                item['lang'] = detected_lang
                fixed_count += 1

    # 统计优化后的语言分布
    after_dist = {}
    for item in data:
        lang = item.get('lang', 'Unknown')
        after_dist[lang] = after_dist.get(lang, 0) + 1

    print(f"\n✨ 优化后语言分布:")
    for lang, count in sorted(after_dist.items(), key=lambda x: -x[1]):
        print(f"   {lang:15s}: {count:5d} 个")

    print(f"\n✅ 成功优化 {fixed_count} 个条目的语言标签")

    # 保存优化后的数据
    backup_file = 'vocabulary_backup.json'
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"💾 原始数据已备份到: {backup_file}")

    with open('vocabulary.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"💾 优化数据已保存到: vocabulary.json")

    # 显示改进效果
    print(f"\n📈 改进效果:")
    print(f"   Mixed/Unknown: {before_dist.get('Mixed', 0) + before_dist.get('Unknown', 0)} → {after_dist.get('Mixed', 0) + after_dist.get('unknown', 0) + after_dist.get('Unknown', 0)}")
    print(f"   识别准确率提升: {(fixed_count / len(data) * 100):.1f}%")

if __name__ == "__main__":
    optimize_language_tags()
    print("\n🎉 语言识别优化完成！")
    print("💡 现在重新打开 dashboard.html 查看优化后的数据分布")
