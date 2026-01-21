# 🚀 GitHub Pages 部署完整教程

## 📋 目录
1. [准备工作](#准备工作)
2. [创建 GitHub 仓库](#创建-github-仓库)
3. [推送代码](#推送代码)
4. [配置 GitHub Pages](#配置-github-pages)
5. [访问在线版本](#访问在线版本)
6. [日常更新流程](#日常更新流程)
7. [常见问题](#常见问题)

---

## 1️⃣ 准备工作

### 检查工具是否安装

**Step 1: 检查 Git**
```bash
git --version
# 应该显示: git version 2.x.x
```

如果没有安装 Git：
- **Windows**: 下载 https://git-scm.com/download/win
- **Mac**: `brew install git`
- **Linux**: `sudo apt-get install git`

**Step 2: 配置 Git 用户信息**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Step 3: 检查 GitHub 账号**
- 访问 https://github.com/
- 如果没有账号，注册一个（免费）

---

## 2️⃣ 创建 GitHub 仓库

### 方式 A: 通过网页创建（推荐新手）

**Step 1: 登录 GitHub**
- 访问 https://github.com/
- 登录你的账号

**Step 2: 创建新仓库**
1. 点击右上角 `+` → `New repository`
2. 填写信息：
   ```
   Repository name: polyglot-matrix
   Description: AI-powered multilingual vocabulary learning system

   ✅ Public (选择公开，才能用 GitHub Pages)
   ❌ 不要勾选 "Add a README file"
   ❌ 不要选择 .gitignore 模板
   ```
3. 点击 `Create repository`

**Step 3: 记录仓库地址**
```
你会看到类似这样的地址:
https://github.com/你的用户名/polyglot-matrix.git
```

---

## 3️⃣ 推送代码到 GitHub

### Step 1: 初始化 Git 仓库

打开终端，进入项目文件夹：

```bash
cd "C:\Users\lenovo\OneDrive\桌面\langue"

# 初始化 Git
git init

# 查看状态
git status
```

### Step 2: 创建 .gitignore 文件

**重要！** 避免上传敏感信息和临时文件。

我已经为你准备好了 `.gitignore` 文件（见下一步）。

### Step 3: 添加文件到 Git

```bash
# 添加所有文件
git add .

# 查看将要提交的文件
git status
```

### Step 4: 创建第一个提交

```bash
# 提交到本地仓库
git commit -m "Initial commit: Polyglot Matrix v2.0 with AI features"
```

### Step 5: 连接到 GitHub 远程仓库

```bash
# 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/你的用户名/polyglot-matrix.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

**如果提示输入用户名和密码:**
- 用户名: 你的 GitHub 用户名
- 密码: 使用 **Personal Access Token**（不是登录密码）

**如何获取 Personal Access Token:**
1. GitHub 右上角头像 → Settings
2. 左侧菜单 → Developer settings → Personal access tokens → Tokens (classic)
3. Generate new token
4. 勾选 `repo` 权限
5. 复制生成的 token（只显示一次，保存好！）

---

## 4️⃣ 配置 GitHub Pages

### Step 1: 进入仓库设置

1. 访问你的仓库: `https://github.com/你的用户名/polyglot-matrix`
2. 点击 `Settings` (设置)
3. 左侧菜单找到 `Pages`

### Step 2: 配置发布源

在 **Build and deployment** 部分:

```
Source: Deploy from a branch
Branch: main
Folder: / (root)
```

点击 `Save`

### Step 3: 等待部署

- GitHub 会自动构建和部署
- 等待 1-2 分钟
- 刷新页面，会看到绿色提示：
  ```
  ✅ Your site is live at https://你的用户名.github.io/polyglot-matrix/
  ```

---

## 5️⃣ 访问在线版本

### 你的网站地址

```
🌐 Dashboard:
https://你的用户名.github.io/polyglot-matrix/dashboard.html

🧠 Semantic Search:
https://你的用户名.github.io/polyglot-matrix/semantic_search.html

📋 Index:
https://你的用户名.github.io/polyglot-matrix/index.html
```

### 设置自定义域名（可选）

如果你有自己的域名（如 `vocab.example.com`）:

1. 在 GitHub Pages 设置页面
2. Custom domain 输入你的域名
3. 在域名 DNS 设置中添加 CNAME 记录指向 `你的用户名.github.io`

---

## 6️⃣ 日常更新流程

### 场景 1: 添加了新单词

```bash
# 1. 查看修改
git status

# 2. 添加修改的文件
git add vocabulary.json

# 3. 提交
git commit -m "Add 10 new Spanish words"

# 4. 推送到 GitHub
git push

# 5. 等待 1-2 分钟，GitHub Pages 自动更新
```

### 场景 2: 修改了页面样式

```bash
git add dashboard.html
git commit -m "Update dashboard UI colors"
git push
```

### 场景 3: 批量更新多个文件

```bash
# 添加所有修改
git add .

# 提交并说明修改内容
git commit -m "Update: new words + optimize language detection"

# 推送
git push
```

---

## 7️⃣ 高级功能

### 功能 1: 自动化部署脚本

我会为你创建 `deploy.bat`，使用方法：

```bash
# 一键提交并部署
deploy.bat "Add new vocabulary"
```

### 功能 2: GitHub Actions 自动化

创建 `.github/workflows/deploy.yml`，实现：
- 自动运行测试
- 自动优化图片
- 自动生成统计报告

### 功能 3: 分支管理

```bash
# 创建开发分支
git checkout -b dev

# 在 dev 分支上工作
# ... 添加新功能 ...

# 切换回主分支
git checkout main

# 合并开发分支
git merge dev

# 推送
git push
```

---

## 🐛 常见问题

### Q1: 推送时提示 "Permission denied"
**A:** 检查 Personal Access Token 是否正确配置

```bash
# 重新设置远程仓库 URL（包含 token）
git remote set-url origin https://TOKEN@github.com/用户名/仓库名.git
```

### Q2: GitHub Pages 显示 404
**A:** 检查以下几点：
1. 仓库是否设置为 Public
2. GitHub Pages 是否已启用
3. 文件名大小写是否正确（`Dashboard.html` ≠ `dashboard.html`）
4. 等待几分钟让部署完成

### Q3: 修改后网站没有更新
**A:**
1. 清除浏览器缓存 (Ctrl + Shift + R)
2. 检查 GitHub Actions 是否部署成功（仓库的 Actions 标签）
3. 等待 5-10 分钟

### Q4: Semantic Search 在线版加载很慢
**A:** TensorFlow.js 模型约 50MB，首次加载需要时间。可以：
1. 添加 Loading 进度条
2. 使用 Service Worker 缓存模型
3. 考虑使用更小的模型

### Q5: 如何回退到之前的版本？
**A:**
```bash
# 查看提交历史
git log

# 回退到指定版本
git reset --hard commit_id

# 强制推送
git push -f
```

---

## 📊 部署检查清单

部署前确保：

- [ ] 已创建 `.gitignore` 文件
- [ ] 已删除敏感信息（API Keys）
- [ ] 已测试本地功能正常
- [ ] 已优化文件大小（压缩图片等）
- [ ] 已更新 README.md

部署后确认：

- [ ] 所有页面可以正常打开
- [ ] 图表正确渲染
- [ ] 搜索功能正常
- [ ] 移动端显示正常
- [ ] 浏览器控制台无错误

---

## 🎨 可选优化

### 优化 1: 添加自定义域名

```
1. 购买域名（Namecheap, GoDaddy 等）
2. DNS 设置添加 CNAME 记录
3. GitHub Pages 设置中填写域名
```

### 优化 2: 启用 HTTPS

```
GitHub Pages 自动提供 HTTPS
勾选 "Enforce HTTPS" 选项
```

### 优化 3: 添加 Google Analytics

在 `dashboard.html` 中添加跟踪代码，了解访问数据。

### 优化 4: SEO 优化

```html
<!-- 在每个 HTML 的 <head> 中添加 -->
<meta name="description" content="AI-powered multilingual vocabulary learning system">
<meta name="keywords" content="language learning, vocabulary, AI, multilingual">
<meta property="og:title" content="Polyglot Matrix">
<meta property="og:image" content="https://你的域名/preview.png">
```

---

## 🔗 相关资源

- **GitHub Pages 文档**: https://docs.github.com/pages
- **Git 教程**: https://git-scm.com/book/zh/v2
- **Markdown 指南**: https://www.markdownguide.org/
- **GitHub Actions**: https://docs.github.com/actions

---

## 📞 获取帮助

如果遇到问题：
1. 检查 GitHub Actions 日志
2. 查看浏览器控制台错误
3. 参考 GitHub Pages 故障排除文档
4. 在仓库创建 Issue

---

**🎉 恭喜！你的 Polyglot Matrix 现在已经在线上运行了！**

下一步:
- 阅读 `WORKFLOW_GUIDE.md` 学习日常添加单词
- 分享你的项目链接给朋友
- 在 GitHub 添加 Star ⭐
