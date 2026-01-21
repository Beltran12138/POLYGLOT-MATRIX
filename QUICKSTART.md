# ⚡ 5 分钟快速入门指南

> 从零开始，快速掌握 Polyglot Matrix 的使用

---

## 🎯 场景 1: 我想添加新单词

### 方法 A: 最快速（1 分钟）

**使用交互式工具:**
```bash
python quick_add.py
```

按提示输入:
```
📝 单词: perseverance
🌍 语言: en
🏷️  词性: n.
📖 释义: 坚持不懈
✅ 已添加
```

---

### 方法 B: 批量添加（适合 10+ 个单词）

**Step 1: 创建文本文件** `my_words.txt`
```txt
perseverance n.坚持不懈&毅力
resiliente adj.有韧性的&适应力强的
komorebi 日.木漏れ日&阳光透过树叶
```

**Step 2: 运行解析**
```bash
python extract_vocab.py
```

**Step 3: 合并到主数据库**
```bash
python merge_vocab.py vocabulary.json
```

---

### 方法 C: 手动编辑（最直接）

直接打开 `vocabulary.json`，在末尾添加:
```json
    {
        "word": "perseverance",
        "lang": "en",
        "type": "n.",
        "def": "坚持不懈&毅力"
    }
]
```

---

## 🚀 场景 2: 我想部署到 GitHub

### 完整流程（首次部署）

**Step 1: 初始化 Git**
```bash
git init
git add .
git commit -m "Initial commit"
```

**Step 2: 创建 GitHub 仓库**
1. 访问 https://github.com/new
2. 仓库名: `polyglot-matrix`
3. 选择 Public
4. 点击 Create

**Step 3: 推送代码**
```bash
git remote add origin https://github.com/你的用户名/polyglot-matrix.git
git branch -M main
git push -u origin main
```

**Step 4: 启用 GitHub Pages**
1. 仓库 → Settings → Pages
2. Source: `main` 分支
3. Folder: `/` (root)
4. Save

**完成！** 访问: `https://你的用户名.github.io/polyglot-matrix/dashboard.html`

---

### 日常更新（超简单）

**方式 1: 使用自动化脚本（推荐）**
```bash
deploy.bat "Add new words"
```
一行命令搞定！

**方式 2: 手动命令**
```bash
git add .
git commit -m "Update vocabulary"
git push
```

---

## 📊 场景 3: 我想查看学习数据

### 本地查看

**双击打开:**
- `dashboard.html` - 数据仪表盘
- `semantic_search.html` - AI 搜索

**或使用启动器:**
```bash
quick_demo.bat
# 选择 [1] 打开 Dashboard
```

### 在线查看

访问你的 GitHub Pages 地址:
```
https://你的用户名.github.io/polyglot-matrix/dashboard.html
```

---

## 🎴 场景 4: 我想生成 Anki 卡片

**Step 1: 安装依赖（首次）**
```bash
pip install genanki edge-tts
```

**Step 2: 生成卡片**
```bash
python generate_anki.py
```

**Step 3: 导入 Anki**
1. 打开 Anki
2. 文件 → 导入
3. 选择 `polyglot_deck.apkg`
4. 开始复习！

---

## 🔄 完整工作流（推荐）

### 每天晚上 10 分钟

```bash
# 🚀 超级快捷方式：一键完成所有步骤！
update_all.bat

# 这个脚本会:
# 1. 解析今天记录的单词
# 2. 验证数据完整性
# 3. 生成 Anki 卡片（可选）
# 4. 部署到 GitHub（可选）
```

### 手动步骤（如果你想了解细节）

**第1步: 添加单词（早上5分钟）**
```bash
# 随手记录到 daily.txt
notepad daily.txt

# 内容示例:
# perseverance n.坚持不懈
# resiliente adj.有韧性的
```

**第2步: 处理数据（晚上3分钟）**
```bash
# 解析新单词
python extract_vocab.py

# 合并到主数据库
python merge_vocab.py vocabulary.json

# 验证数据
python test_data.py
```

**第3步: 生成学习材料（2分钟）**
```bash
# 生成 Anki 卡片
python generate_anki.py

# 或生成海报
python word_poster_generator.py
```

**第4步: 同步到云端（1分钟）**
```bash
deploy.bat "Add daily words"
```

---

## 🛠️ 常用命令速查

| 任务 | 命令 | 说明 |
|------|------|------|
| 快速添加单词 | `python quick_add.py` | 交互式添加 |
| 批量解析 | `python extract_vocab.py` | 从 .txt 解析 |
| 合并数据 | `python merge_vocab.py new.json` | 合并新单词 |
| 测试数据 | `python test_data.py` | 验证完整性 |
| 生成 Anki | `python generate_anki.py` | 制作卡片 |
| 生成海报 | `python word_poster_generator.py` | Instagram 海报 |
| 部署到 Git | `deploy.bat "message"` | 一键部署 |
| 全流程更新 | `update_all.bat` | 一键完成所有 |

---

## 💡 实用技巧

### 技巧 1: 设置每日提醒

**Windows 任务计划:**
1. 打开"任务计划程序"
2. 创建基本任务
3. 触发器: 每天晚上 9:00
4. 操作: 运行 `update_all.bat`

### 技巧 2: 云端同步

**使用 OneDrive/Google Drive:**
```bash
# 将项目文件夹放在云盘
C:\Users\你的用户名\OneDrive\polyglot-matrix\

# 多设备自动同步
```

### 技巧 3: 快捷方式

**创建桌面快捷方式:**
- 右键 `dashboard.html` → 发送到 → 桌面快捷方式
- 右键 `quick_add.py` → 发送到 → 桌面快捷方式

### 技巧 4: 语音输入（未来功能）

```bash
# 使用 Windows 语音识别
Win + H
# 说话 → 自动转文字 → 粘贴到 .txt 文件
```

---

## ❓ 常见问题 1 分钟解决

### Q: 添加单词后 Dashboard 没更新？
```bash
# 刷新浏览器缓存
Ctrl + Shift + R
```

### Q: JSON 格式错误？
```bash
# 使用在线验证工具
打开 https://jsonlint.com/
粘贴你的 JSON 内容
查看错误提示
```

### Q: Git 推送失败？
```bash
# 检查网络
ping github.com

# 检查凭据
git config user.name
git config user.email

# 重新设置远程仓库
git remote -v
git remote set-url origin https://你的token@github.com/用户名/仓库.git
```

### Q: Anki 生成太慢？
```bash
# 只生成最近100个单词
# 编辑 generate_anki.py
# 修改第 71 行: for item in vocabdata[:100]
```

---

## 📞 获取更多帮助

- 📖 [完整工作流指南](WORKFLOW_GUIDE.md)
- 🚀 [GitHub 部署详解](GITHUB_DEPLOY.md)
- 🧪 [测试报告](TEST_REPORT.md)
- 📦 [项目总结](PROJECT_SUMMARY.md)

---

## 🎯 下一步

- [ ] 阅读 [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) 了解更多技巧
- [ ] 部署到 GitHub 并分享链接
- [ ] 生成第一批 Anki 卡片开始复习
- [ ] 加入社区（待建立）

---

**🎉 开始你的语言学习之旅吧！**

有问题？查看详细文档或在 GitHub 提 Issue。
