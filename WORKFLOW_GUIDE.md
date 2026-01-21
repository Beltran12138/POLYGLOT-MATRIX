# 📝 Polyglot Matrix - 日常使用工作流

## 🎯 添加新单词的 3 种方法

---

## 方法 1️⃣: 手动编辑 JSON（最快速）

### 适用场景
- 临时添加 1-5 个单词
- 已知完整信息（语言、词性、释义）

### 操作步骤

**Step 1: 打开 vocabulary.json**
```bash
# 用任意文本编辑器打开
notepad vocabulary.json
# 或 VS Code
code vocabulary.json
```

**Step 2: 在数组末尾添加新条目**

找到文件末尾的 `]`，在最后一个条目后添加：

```json
    {
        "word": "perseverance",
        "lang": "en",
        "type": "n.",
        "def": "坚持不懈&毅力"
    },
    {
        "word": "resiliente",
        "lang": "es",
        "type": "adj.",
        "def": "有韧性的&适应力强的"
    }
]
```

**⚠️ 注意事项:**
- 每个条目之间用 `,` 分隔
- 最后一个条目后**不要**加逗号
- 确保 JSON 格式正确（使用 JSON 验证器）

**Step 3: 验证数据**
```bash
python test_data.py
# 会显示新的总词汇量
```

**Step 4: 刷新浏览器查看**
```
按 F5 刷新 dashboard.html
新单词会自动显示在统计中
```

---

## 方法 2️⃣: 文本文件批量导入（推荐）

### 适用场景
- 每天记录 10+ 个单词
- 从笔记软件导出数据
- 习惯用纯文本记录

### 操作步骤

**Step 1: 创建文本文件**

在 `langue` 文件夹中创建 `new_words.txt`：

```txt
perseverance n.坚持不懈&毅力
resiliente adj.有韧性的&适应力强的
komorebi 日.木漏れ日&从树叶缝隙透过的阳光
abogado m.律师&辩护人
```

**格式规则:**
```
单词 词性.释义
单词 词性.释义1&释义2&释义3
```

**Step 2: 运行解析脚本**

```bash
# 使用原始 Regex 解析器（免费、快速）
python extract_vocab.py

# 或使用 AI 增强解析器（需要 API Key）
export ANTHROPIC_API_KEY='your_key'
python extract_vocab_ai.py
```

**Step 3: 合并到主数据库**

解析后会生成 `vocabulary.json`，你需要手动合并：

```python
# 快速合并脚本
python -c "
import json

# 读取原数据
with open('vocabulary.json', 'r', encoding='utf-8') as f:
    old_data = json.load(f)

# 读取新数据（假设在 new_vocabulary.json）
with open('new_vocabulary.json', 'r', encoding='utf-8') as f:
    new_data = json.load(f)

# 合并并去重
combined = old_data + new_data
# 基于单词去重
unique = {v['word']: v for v in combined}.values()

# 保存
with open('vocabulary.json', 'w', encoding='utf-8') as f:
    json.dump(list(unique), f, ensure_ascii=False, indent=2)

print(f'合并完成！总词汇: {len(unique)}')
"
```

---

## 方法 3️⃣: 使用 AI 增强解析（最智能）

### 适用场景
- 笔记格式混乱、不规范
- 需要自动补全词源、例句
- 想要智能语言识别

### 前置准备

**获取 Claude API Key:**
1. 访问 https://console.anthropic.com/
2. 注册账号
3. 创建 API Key
4. 复制 Key

**设置环境变量:**

```bash
# Windows CMD
set ANTHROPIC_API_KEY=sk-ant-api03-xxxxx

# Windows PowerShell
$env:ANTHROPIC_API_KEY="sk-ant-api03-xxxxx"

# Mac/Linux
export ANTHROPIC_API_KEY='sk-ant-api03-xxxxx'
```

### 操作步骤

**Step 1: 准备文本文件**

创建 `my_notes.txt`，格式可以很随意：

```txt
perseverance - 坚持不懈
resiliente (西语) 有韧性的
木漏れ日 = komorebi = 阳光透过树叶
abogado 律师
```

**Step 2: 运行 AI 解析**

```bash
python extract_vocab_ai.py
```

**输出示例:**
```json
{
    "word": "perseverance",
    "lang": "en",
    "type": "n.",
    "def": "坚持不懈&毅力",
    "etymology": "源自拉丁语 perseverare (坚持到底)",
    "example": "Her perseverance led to success.",
    "synonyms": ["persistence", "tenacity"],
    "difficulty": 4
}
```

**Step 3: 合并数据**

使用上面方法 2 中的合并脚本。

---

## 🔄 完整工作流（每日推荐）

### 早上：记录新单词（5 分钟）

```bash
# 1. 打开文本编辑器
notepad daily_words.txt

# 2. 随手记录遇到的生词
# 格式随意，AI 会帮你整理
```

### 晚上：处理和复习（10 分钟）

```bash
# 1. 解析今天的单词
python extract_vocab_ai.py

# 2. 合并到主数据库
python merge_vocab.py  # 我们稍后创建这个脚本

# 3. 生成 Anki 卡片
python generate_anki.py

# 4. 打开 Dashboard 查看进度
start dashboard.html
```

---

## 🛠️ 自动化工具脚本

### 1. 合并词汇脚本 (`merge_vocab.py`)

我会为你创建这个脚本，使用方法：

```bash
# 自动合并新单词到主数据库
python merge_vocab.py new_vocabulary.json

# 或指定多个文件
python merge_vocab.py file1.json file2.json file3.json
```

### 2. 快速添加脚本 (`quick_add.py`)

交互式添加单词：

```bash
python quick_add.py

# 会提示输入:
# > 单词: perseverance
# > 语言 (en/es/fr/ja/zh): en
# > 词性: n.
# > 释义: 坚持不懈
# > 继续添加? (y/n): n
#
# ✅ 已添加 1 个单词到 vocabulary.json
```

---

## 📊 数据维护建议

### 每周任务
- ✅ 运行 `test_data.py` 检查数据完整性
- ✅ 运行 `fix_language_detection.py` 优化语言识别
- ✅ 备份 `vocabulary.json` 到云端

### 每月任务
- ✅ 生成本月 Anki 卡片复习
- ✅ 生成学习报告（词汇增长曲线）
- ✅ 清理重复或错误条目

---

## 🔧 常见问题

### Q: 添加单词后 Dashboard 没有更新？
**A:** 刷新浏览器缓存 (Ctrl + Shift + R)

### Q: JSON 格式错误怎么办？
**A:** 使用在线工具验证：https://jsonlint.com/

### Q: 如何删除错误的单词？
**A:**
1. 打开 `vocabulary.json`
2. 搜索该单词
3. 删除整个 `{...}` 块
4. 注意处理逗号

### Q: 如何修改已有单词的信息？
**A:**
1. 打开 `vocabulary.json`
2. 搜索单词
3. 直接修改对应字段
4. 保存并刷新浏览器

---

## 💡 高级技巧

### 技巧 1: 从 Anki 导出到本系统

```bash
# 1. Anki 导出为 CSV
# 文件 -> 导出 -> Notes in Plain Text

# 2. 转换 CSV 到 JSON（我们创建转换脚本）
python convert_anki_csv.py anki_export.csv
```

### 技巧 2: 批量生成海报

```bash
# 为最近添加的 10 个单词生成海报
python word_poster_generator.py --recent 10
```

### 技巧 3: 语音输入（未来功能）

```bash
# 使用语音识别快速添加（需要 speech_recognition 库）
python voice_add.py
# 说话 → 自动转文字 → AI 解析 → 添加到数据库
```

---

## 📱 移动端工作流

### 方案 1: 云同步
1. 将 `langue` 文件夹同步到 OneDrive/Google Drive
2. 手机上编辑 `new_words.txt`
3. 电脑端自动同步并处理

### 方案 2: GitHub + Termux
1. 推送到 GitHub
2. 手机 Termux 克隆仓库
3. 编辑文件并推送
4. 电脑端拉取更新

---

## 🎯 最佳实践

✅ **DO (推荐做法):**
- 每天固定时间记录单词
- 使用统一的格式（便于解析）
- 定期备份数据
- 使用 Git 版本控制
- 及时复习（Anki 间隔重复）

❌ **DON'T (避免做法):**
- 不要直接修改 `vocabulary.json` 的结构
- 不要删除备份文件
- 不要在多个地方同时编辑（会冲突）
- 不要忘记运行测试脚本验证

---

**下一步:** 阅读 `GITHUB_DEPLOY.md` 学习如何部署到 GitHub Pages
