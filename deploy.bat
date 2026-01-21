@echo off
chcp 65001 >nul
title Polyglot Matrix - Git Deploy

REM ==========================================
REM 🚀 一键部署到 GitHub
REM ==========================================

echo.
echo ========================================
echo   🚀 Git Deploy - 自动部署工具
echo ========================================
echo.

REM 检查是否传入提交信息
if "%~1"=="" (
    set /p commit_msg="💬 请输入提交信息: "
) else (
    set commit_msg=%~1
)

if "%commit_msg%"=="" (
    set commit_msg=Update vocabulary and files
)

echo.
echo 📋 提交信息: %commit_msg%
echo.

REM 检查 Git 状态
echo 🔍 检查文件变更...
git status --short

echo.
set /p confirm="❓ 确认提交并推送? (y/n): "

if /i not "%confirm%"=="y" (
    echo.
    echo ❌ 已取消部署
    pause
    exit /b
)

echo.
echo ==========================================
echo 📦 开始部署...
echo ==========================================

REM Step 1: 添加所有文件
echo.
echo [1/4] 📁 添加文件到 Git...
git add .

REM Step 2: 提交
echo [2/4] 💾 创建提交...
git commit -m "%commit_msg%"

if errorlevel 1 (
    echo.
    echo ⚠️  没有需要提交的更改
    echo.
    pause
    exit /b
)

REM Step 3: 推送到 GitHub
echo [3/4] 🚀 推送到 GitHub...
git push

if errorlevel 1 (
    echo.
    echo ❌ 推送失败！请检查:
    echo    1. 网络连接
    echo    2. GitHub 凭据
    echo    3. 远程仓库配置
    echo.
    pause
    exit /b
)

REM Step 4: 完成
echo [4/4] ✅ 部署完成！
echo.
echo ==========================================
echo   🎉 部署成功！
echo ==========================================
echo.
echo 📊 统计信息:
git log -1 --stat
echo.
echo 💡 访问在线版本:
echo    Dashboard: https://你的用户名.github.io/polyglot-matrix/dashboard.html
echo    Search:    https://你的用户名.github.io/polyglot-matrix/semantic_search.html
echo.
echo ⏰ GitHub Pages 通常需要 1-2 分钟更新
echo.

pause
