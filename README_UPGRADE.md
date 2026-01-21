# 🚀 Polyglot Matrix - 升级指南

## 项目架构升级

从传统的 Regex 解析 → AI 驱动的多语言知识管理系统

---

## ✨ 新功能概览

### 1️⃣ AI 语义解析 (`extract_vocab_ai.py`)

**替代原有的 `extract_vocab.py`**

**核心改进：**
- ✅ 使用 Claude API 进行智能解析
- ✅ 自动语言检测（ISO 639-1 标准）
- ✅ 补全词根词源 (Etymology)
- ✅ 生成例句
- ✅ 难度评级 (1-5)

**使用方法：**
```bash
# 设置环境变量
export ANTHROPIC_API_KEY='your_api_key_here'

# 运行 AI 解析
python extract_vocab_ai.py
```

**输入示例：**
```
abogado m.律师&中间人
abide v.遵守&忍受
```

**输出示例：**
```json
{
    "word": "abogado",
    "lang": "es",
    "type": "m.",
    "def": "律师&中间人",
    "etymology": "源自拉丁语 advocatus (辩护人)",
    "example": "El abogado defendió su caso brillantemente.",
    "synonyms": ["defensor", "letrado"],
    "difficulty": 3
}
```

---

### 2️⃣ 语义搜索引擎 (`semantic_search.html`)

**特性：**
- 🧠 基于 Universal Sentence Encoder
- 🌐 跨语言语义检索
- 📊 相似度评分可视化

**示例查询：**
- "关于悲伤的形容词" → 返回 `melancholy`, `triste`, `切ない`
- "表达坚持的动词" → 返回 `persevere`, `persistir`, `abide`

**本地运行：**
```bash
# 直接在浏览器中打开
open semantic_search.html
```

---

### 3️⃣ 数据分析仪表盘 (`dashboard.html`)

**可视化内容：**
- 📊 语言分布饼图
- 🏷️ 词性柱状图
- 🗺️ 语言能力雷达图
- 🎯 实时统计面板

**设计亮点：**
- Cyberpunk 美学（霓虹渐变 + 毛玻璃）
- 响应式设计
- Chart.js 驱动的动态图表

**效果预览：**
```
┌─────────────────────────────┐
│  TOTAL VOCABULARY: 1247     │
│  LANGUAGES: 5               │
│  AVG DIFFICULTY: 3.2        │
└─────────────────────────────┘
```

---

### 4️⃣ Anki 自动制卡 (`generate_anki.py`)

**功能：**
- 🎴 生成 .apkg 卡片包
- 🔊 集成 Edge TTS 原生发音
- 🎨 高颜值卡片模板

**生成流程：**
```bash
pip install genanki edge-tts
python generate_anki.py
```

**输出：**
- `polyglot_deck.apkg` (双击导入 Anki)
- `anki_audio/` (发音文件夹)

**卡片模板：**
```
┌──────────────────────────┐
│        abogado           │  ← 正面
│     Español · m.         │
│         🔊               │
└──────────────────────────┘

┌──────────────────────────┐
│  📖 律师&中间人           │  ← 背面
│  💡 El abogado defiende  │
│  🌱 源自拉丁语 advocatus │
└──────────────────────────┘
```

---

### 5️⃣ 社交媒体海报 (`word_poster_generator.py`)

**用途：**
- 📸 生成 Instagram 风格单词卡
- 🎨 根据语言自动配色
- ✨ 渐变 + 噪点质感

**使用：**
```bash
pip install Pillow
python word_poster_generator.py
```

**输出示例：**
```
word_posters/
├── abogado_poster.png
├── abide_poster.png
└── ...
```

---

## 🛠️ 技术栈对比

| 模块         | 原方案                | 升级方案                          |
|--------------|-----------------------|-----------------------------------|
| 数据解析     | Regex               | Claude API (LLM)                 |
| 搜索         | 简单字符串匹配       | 向量语义搜索 (USE)                |
| 可视化       | 无                   | Chart.js + Cyberpunk UI          |
| 记忆闭环     | 无                   | Anki + TTS                       |
| 内容营销     | 无                   | Pillow 自动海报                   |

---

## 📂 文件结构

```
langue/
├── extract_vocab.py          # [旧] 原始正则解析
├── extract_vocab_ai.py       # [新] AI 增强解析
├── vocabulary.json           # 原始数据
├── vocabulary_enhanced.json  # AI 增强数据
├── index.html                # [旧] 基础展示页
├── semantic_search.html      # [新] 语义搜索
├── dashboard.html            # [新] 数据仪表盘
├── generate_anki.py          # [新] Anki 生成器
├── word_poster_generator.py  # [新] 海报生成器
├── requirements.txt          # 依赖清单
└── README_UPGRADE.md         # 本文档
```

---

## 🚀 快速开始

### Step 1: 安装依赖
```bash
pip install -r requirements.txt
```

### Step 2: 配置 API Key
```bash
# Windows
set ANTHROPIC_API_KEY=your_key_here

# macOS/Linux
export ANTHROPIC_API_KEY='your_key_here'
```

### Step 3: 运行 AI 解析
```bash
python extract_vocab_ai.py
```

### Step 4: 打开可视化页面
```bash
# 方式1: 直接用浏览器打开
open dashboard.html

# 方式2: 启动本地服务器
python -m http.server 8000
# 访问 http://localhost:8000/dashboard.html
```

---

## 💡 高级用法

### 批量处理多个文本文件
```python
# 在 extract_vocab_ai.py 中修改
SOURCE_FOLDER = './my_notes'  # 指向包含 .txt 文件的文件夹
```

### 自定义 Anki 卡片模板
编辑 `generate_anki.py:36-75` 的 `templates` 部分

### 修改海报配色
编辑 `word_poster_generator.py:16-43` 的 `THEME_COLORS`

---

## 🎨 设计哲学

### 色彩系统
```
英语 (en): 紫蓝 (#667eea) - 理性与科技
西语 (es): 粉红 (#f093fb) - 热情与浪漫
法语 (fr): 青蓝 (#4facfe) - 优雅与艺术
日语 (ja): 樱花粉 (#fa709a) - 传统与美学
中文 (zh): 青紫 (#30cfd0) - 深邃与智慧
```

### 字体搭配
- **标题**: Space Grotesk (几何现代)
- **代码**: JetBrains Mono (等宽优雅)
- **中文**: Noto Sans SC (清晰易读)

---

## 🔮 未来规划

### Phase 2 功能
- [ ] Chrome 扩展（划词自动添加到词库）
- [ ] 间隔重复算法优化（SM-2 改进版）
- [ ] 多模态学习（图片 + 语音联想）
- [ ] 社区共享词库（GitHub Gist 同步）

### Phase 3 商业化
- [ ] Notion/Obsidian 插件
- [ ] Premium 订阅（无限 AI 解析）
- [ ] 白标定制服务

---

## 🤝 贡献指南

欢迎提交 PR！重点方向：
1. 新语言支持（韩语、意大利语等）
2. 更精准的词性识别算法
3. 移动端适配
4. 更多卡片模板

---

## 📄 License

MIT License - 自由使用，保留署名

---

## 🙏 鸣谢

- **Anthropic Claude API** - AI 解析核心
- **TensorFlow.js** - 浏览器端机器学习
- **Genanki** - Anki 卡片生成
- **Edge TTS** - 免费语音合成

---

**Built with 💜 by Language Learners, for Language Learners**

*让语言学习从机械记忆，进化为智能探索。*
