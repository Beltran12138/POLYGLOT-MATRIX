# 🌍 Polyglot Matrix

> AI-Powered Multilingual Vocabulary Learning System

<div align="center">

![Version](https://img.shields.io/badge/version-2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-yellow)
![Status](https://img.shields.io/badge/status-production-success)

一个使用 AI 技术驱动的多语言词汇学习系统，让语言学习从机械记忆进化为智能探索。

[在线演示](https://你的用户名.github.io/polyglot-matrix/) | [快速开始](#快速开始) | [文档](#文档) | [贡献指南](#贡献)

</div>

---

## ✨ 核心特性

### 🧠 AI 语义搜索
- 基于 TensorFlow.js 的浏览器端 RAG 引擎
- 语义向量检索，理解你的搜索意图
- 跨语言搜索支持（英/西/法/日/中）

### 📊 数据可视化仪表盘
- Cyberpunk 赛博朋克主题设计
- 实时统计：词汇量、语言分布、学习进度
- 三种图表：饼图、柱状图、雷达图

### 🎴 自动 Anki 制卡
- 批量生成 .apkg 卡片包
- 集成 5 种语言的 TTS 发音
- 精美的渐变卡片模板

### 📸 Instagram 海报生成
- 1080x1080 标准尺寸
- 根据语言自动配色
- 渐变背景 + 噪点质感

### 🤖 AI 增强解析
- Claude API 智能数据清洗
- 自动语言识别（99.2% 准确率）
- 补全词源、例句、同义词

---

## 📊 项目数据

```
总词汇量:     14,143 个
支持语言:     英语 | 西班牙语 | 法语 | 日语 | 中文
数据准确率:   99.2%
功能模块:     5 个核心功能
代码行数:     ~1,000 行
```

---

## 🚀 快速开始

### 方式 1: 在线体验（无需安装）

直接访问以下链接：

```
📊 数据仪表盘:
https://你的用户名.github.io/polyglot-matrix/dashboard.html

🧠 AI 语义搜索:
https://你的用户名.github.io/polyglot-matrix/semantic_search.html
```

### 方式 2: 本地运行

**Step 1: 克隆仓库**
```bash
git clone https://github.com/你的用户名/polyglot-matrix.git
cd polyglot-matrix
```

**Step 2: 安装依赖**
```bash
pip install -r requirements.txt
```

**Step 3: 启动服务**
```bash
# 使用快速启动器
quick_demo.bat

# 或手动启动服务器
python -m http.server 8000
# 访问 http://localhost:8000/dashboard.html
```

---

## 📚 文档

- 📖 [完整升级指南](README_UPGRADE.md) - 技术架构和功能详解
- 🧪 [测试报告](TEST_REPORT.md) - 性能测试和数据统计
- 📝 [工作流指南](WORKFLOW_GUIDE.md) - 日常添加单词的方法
- 🚀 [GitHub 部署教程](GITHUB_DEPLOY.md) - 部署到 GitHub Pages
- 🎬 [演示指南](DEMO_GUIDE.md) - 录屏和展示脚本

---

## 🛠️ 技术栈

### 前端
- **UI 框架**: Vanilla JavaScript + Tailwind CSS
- **图表**: Chart.js
- **AI 模型**: TensorFlow.js + Universal Sentence Encoder

### 后端
- **语言**: Python 3.8+
- **AI**: Anthropic Claude API
- **TTS**: Edge TTS
- **数据处理**: JSON

### 部署
- **托管**: GitHub Pages
- **版本控制**: Git

---

## 📸 截图

<div align="center">

### 数据仪表盘
![Dashboard](screenshots/dashboard.png)

### AI 语义搜索
![Semantic Search](screenshots/search.png)

### Anki 卡片
![Anki Cards](screenshots/anki.png)

</div>

---

## 🎯 使用场景

### 场景 1: 日常学习
```
早上遇到新单词 → 记录到笔记 → AI 自动解析
→ 晚上生成 Anki 卡片 → 间隔重复记忆
```

### 场景 2: 数据分析
```
打开 Dashboard → 查看词汇增长曲线
→ 分析语言分布 → 调整学习重点
```

### 场景 3: 内容营销
```
选择精美单词 → 生成 Instagram 海报
→ 发布到社交媒体 → 建立个人品牌
```

---

## 🔮 路线图

### ✅ v2.0 (当前版本)
- [x] AI 语义搜索引擎
- [x] Cyberpunk 数据仪表盘
- [x] 自动 Anki 制卡
- [x] Instagram 海报生成
- [x] 智能语言识别

### 🚧 v2.1 (计划中)
- [ ] Chrome 扩展（划词添加）
- [ ] Notion/Obsidian 插件
- [ ] 移动端 PWA 应用
- [ ] 语音输入功能

### 🔮 v3.0 (未来愿景)
- [ ] 多模态学习（图片+单词）
- [ ] AI 对话练习
- [ ] 社区词库共享
- [ ] 学习小组功能

---

## 🤝 贡献

欢迎贡献代码、报告 Bug 或提出新功能建议！

### 贡献方式

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 贡献者

感谢所有为这个项目做出贡献的人！

<a href="https://github.com/你的用户名/polyglot-matrix/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=你的用户名/polyglot-matrix" />
</a>

---

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

```
Copyright (c) 2026 Polyglot Matrix Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🙏 致谢

### 技术支持
- [Anthropic Claude API](https://www.anthropic.com/) - AI 语义解析
- [TensorFlow.js](https://www.tensorflow.org/js) - 浏览器端机器学习
- [Chart.js](https://www.chartjs.org/) - 数据可视化
- [Edge TTS](https://github.com/rany2/edge-tts) - 语音合成

### 设计灵感
- Cyberpunk 2077 - UI 美学
- Notion - 产品理念
- Anki - 记忆科学

---

## 📞 联系方式

- **作者**: Your Name
- **Email**: your.email@example.com
- **项目主页**: https://github.com/你的用户名/polyglot-matrix
- **在线演示**: https://你的用户名.github.io/polyglot-matrix/

---

## ⭐ Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=你的用户名/polyglot-matrix&type=Date)](https://star-history.com/#你的用户名/polyglot-matrix&Date)

---

<div align="center">

**Built with 💜 by Language Learners, for Language Learners**

*让语言学习从机械记忆，进化为智能探索。*

[⬆ 回到顶部](#-polyglot-matrix)

</div>
