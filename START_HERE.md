# 👋 从这里开始！

> 欢迎使用 Polyglot Matrix - 你的 AI 语言学习助手

---

## 🚀 3 秒钟快速开始

### 📊 查看数据可视化
**双击打开:** `dashboard.html`

### 📝 添加新单词
**双击运行:** `quick_add.py`

### 🚀 部署到网上
**双击运行:** `deploy.bat`

---

## 📚 我应该先看什么？

### 🔰 新手必读（按顺序）

1. **⚡ [5分钟快速入门](QUICKSTART.md)** ← 从这里开始！
   - 最简单的使用方法
   - 常用命令速查
   - 常见问题解答

2. **📝 [日常工作流指南](WORKFLOW_GUIDE.md)**
   - 如何添加新单词（3种方法）
   - 每日推荐流程
   - 高级技巧

3. **🚀 [GitHub 部署教程](GITHUB_DEPLOY.md)**
   - 完整部署步骤
   - 自动化更新方法
   - 故障排除

---

### 📖 进阶阅读（有时间再看）

4. **📦 [项目总结](PROJECT_SUMMARY.md)**
   - 技术架构详解
   - 功能特性介绍
   - 未来路线图

5. **🧪 [测试报告](TEST_REPORT.md)**
   - 性能基准测试
   - 数据统计分析
   - 功能验证

6. **🎬 [演示指南](DEMO_GUIDE.md)**
   - 录屏脚本
   - 展示技巧
   - PPT 建议

7. **📖 [完整升级指南](README_UPGRADE.md)**
   - 从 v1.0 到 v2.0 的变化
   - 技术细节
   - API 使用说明

---

## 🗂️ 文件导航

### 📄 使用文档（7个）
```
START_HERE.md          ← 你现在在这里
├─ QUICKSTART.md       ← ⭐ 5分钟入门
├─ WORKFLOW_GUIDE.md   ← ⭐ 日常使用
├─ GITHUB_DEPLOY.md    ← ⭐ 部署教程
├─ PROJECT_SUMMARY.md  ← 项目总结
├─ TEST_REPORT.md      ← 测试报告
└─ DEMO_GUIDE.md       ← 演示指南
```

### 🌐 网页文件（3个）
```
dashboard.html          ← ⭐ 数据仪表盘（双击打开）
semantic_search.html    ← ⭐ AI 搜索（双击打开）
index.html              ← 原始词汇列表
```

### 🐍 Python 脚本（8个）
```
quick_add.py            ← ⭐ 快速添加单词
extract_vocab.py        ← 解析文本文件
merge_vocab.py          ← 合并词汇数据
test_data.py            ← ⭐ 测试数据
generate_anki.py        ← 生成 Anki 卡片
word_poster_generator.py ← 生成 Instagram 海报
extract_vocab_ai.py     ← AI 智能解析（需要 API）
fix_language_detection.py ← 优化语言识别
```

### 🛠️ 工具脚本（3个）
```
quick_demo.bat          ← ⭐ 功能菜单（Windows）
deploy.bat              ← ⭐ 一键部署到 GitHub
update_all.bat          ← ⭐ 全流程自动化
```

### 📊 数据文件（2个）
```
vocabulary.json         ← ⭐ 主词汇数据库
vocabulary_backup.json  ← 数据备份
```

### ⚙️ 配置文件（3个）
```
.gitignore              ← Git 忽略规则
requirements.txt        ← Python 依赖
README.md               ← GitHub 项目首页
```

---

## 🎯 根据你的目标选择路径

### 目标 1: 我只想快速添加单词
👉 阅读: [QUICKSTART.md](QUICKSTART.md) > 场景1
👉 使用: `quick_add.py` 或手动编辑 `vocabulary.json`

### 目标 2: 我想看到学习进度
👉 阅读: [QUICKSTART.md](QUICKSTART.md) > 场景3
👉 打开: `dashboard.html`

### 目标 3: 我想部署到网上让别人访问
👉 阅读: [GITHUB_DEPLOY.md](GITHUB_DEPLOY.md)
👉 使用: `deploy.bat`

### 目标 4: 我想用 Anki 复习
👉 阅读: [QUICKSTART.md](QUICKSTART.md) > 场景4
👉 使用: `generate_anki.py`

### 目标 5: 我想了解技术细节
👉 阅读: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
👉 阅读: [README_UPGRADE.md](README_UPGRADE.md)

### 目标 6: 我想贡献代码
👉 阅读: [README.md](README.md) > 贡献指南
👉 Fork 仓库并提交 PR

---

## ⚡ 最快上手路径（5 分钟）

### 第 1 分钟：查看你的数据
```bash
双击 dashboard.html
```
看看你现在有多少单词，哪些语言

### 第 2 分钟：添加一个新单词
```bash
双击 quick_add.py
# 输入: word=test, lang=en, type=n., def=测试
```

### 第 3 分钟：验证数据
```bash
python test_data.py
```
看看数据是否正确

### 第 4 分钟：刷新页面
```bash
刷新 dashboard.html (F5)
```
看到新单词的统计

### 第 5 分钟：（可选）部署到网上
```bash
双击 deploy.bat
# 按提示操作
```

**🎉 恭喜！你已经掌握了基本流程！**

---

## 🆘 遇到问题？

### 常见问题快速解决

| 问题 | 解决方案 | 文档位置 |
|------|----------|----------|
| 不知道怎么添加单词 | 阅读 QUICKSTART.md 场景1 | [链接](QUICKSTART.md) |
| Dashboard 显示错误 | 运行 test_data.py 检查 | [链接](QUICKSTART.md) |
| Git 推送失败 | 查看 GITHUB_DEPLOY.md Q&A | [链接](GITHUB_DEPLOY.md) |
| Anki 生成失败 | pip install genanki edge-tts | [链接](QUICKSTART.md) |
| JSON 格式错误 | https://jsonlint.com 验证 | [链接](WORKFLOW_GUIDE.md) |

### 获取帮助的优先级

1. 先查看 [QUICKSTART.md](QUICKSTART.md) 的常见问题
2. 再查看对应功能的详细文档
3. 运行 `test_data.py` 诊断数据问题
4. 在 GitHub 提 Issue

---

## 📞 联系与支持

- **GitHub Issues**: 报告 Bug 或功能建议
- **项目主页**: https://github.com/你的用户名/polyglot-matrix
- **在线演示**: https://你的用户名.github.io/polyglot-matrix/

---

## 🎁 推荐工作流

### 新手推荐（简单高效）
```
每天:
1. 遇到生词 → 记录到 daily.txt
2. 晚上双击 update_all.bat → 自动处理一切
3. 打开 Anki 复习
```

### 极客推荐（完全掌控）
```
每天:
1. 手动编辑 vocabulary.json 添加单词
2. 运行 test_data.py 验证
3. 运行 generate_anki.py 制卡
4. 运行 deploy.bat 部署
5. 查看 dashboard.html 分析
```

---

## 🌟 提示与技巧

### 💡 Tip 1: 善用快捷键
- 刷新 Dashboard: `Ctrl + Shift + R`（清除缓存）
- 快速搜索文档: `Ctrl + F`

### 💡 Tip 2: 创建桌面快捷方式
把常用文件拖到桌面，一键打开

### 💡 Tip 3: 定时自动化
使用 Windows 任务计划，每天自动运行 `update_all.bat`

### 💡 Tip 4: 云端同步
把整个文件夹放在 OneDrive/Google Drive，多设备同步

---

## 🎓 学习路线

### 第 1 天: 基础使用
- [ ] 阅读 QUICKSTART.md
- [ ] 添加 10 个单词
- [ ] 打开 Dashboard 查看

### 第 1 周: 熟练掌握
- [ ] 阅读 WORKFLOW_GUIDE.md
- [ ] 生成第一批 Anki 卡片
- [ ] 尝试生成海报

### 第 2 周: 进阶功能
- [ ] 部署到 GitHub Pages
- [ ] 使用 AI 解析（如有 API）
- [ ] 自定义配色和模板

### 第 1 月: 形成习惯
- [ ] 每日自动化流程
- [ ] 分析学习数据
- [ ] 分享给朋友

---

## 📈 成功指标

完成这些，说明你已经掌握了 Polyglot Matrix：

- ✅ 能独立添加单词
- ✅ 能查看并理解 Dashboard 数据
- ✅ 能生成 Anki 卡片并复习
- ✅ 能部署到 GitHub Pages
- ✅ 能处理常见错误

---

## 🎉 开始你的旅程！

选择一个目标，打开对应的文档，开始探索吧！

**推荐第一步:**
👉 打开 [QUICKSTART.md](QUICKSTART.md)，花 5 分钟体验核心功能

---

<div align="center">

**Built with 💜 by Language Learners, for Language Learners**

*让语言学习从机械记忆，进化为智能探索*

</div>
