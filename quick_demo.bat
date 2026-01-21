@echo off
chcp 65001 >nul
title Polyglot Matrix - Quick Demo

echo.
echo ========================================
echo   🚀 Polyglot Matrix - 快速演示
echo ========================================
echo.
echo 请选择要测试的模块:
echo.
echo [1] 📊 打开数据仪表盘 (Dashboard)
echo [2] 🧠 打开语义搜索引擎 (Semantic Search)
echo [3] 📋 原始词汇列表 (Index)
echo [4] 🧪 运行数据测试
echo [5] 📸 生成单词海报
echo [6] 🎴 生成 Anki 卡片 (需要依赖)
echo [7] 🔧 优化语言识别
echo [8] 🌐 启动本地服务器
echo [0] ❌ 退出
echo.

set /p choice="请输入选项 (0-8): "

if "%choice%"=="1" (
    echo.
    echo 正在打开 Dashboard...
    start dashboard.html
    goto end
)

if "%choice%"=="2" (
    echo.
    echo 正在打开 Semantic Search...
    echo ⚠️  首次加载需要下载 AI 模型，请耐心等待...
    start semantic_search.html
    goto end
)

if "%choice%"=="3" (
    echo.
    echo 正在打开原始词汇列表...
    start index.html
    goto end
)

if "%choice%"=="4" (
    echo.
    echo 正在运行数据测试...
    python test_data.py
    pause
    goto end
)

if "%choice%"=="5" (
    echo.
    echo 正在启动海报生成器...
    python word_poster_generator.py
    pause
    goto end
)

if "%choice%"=="6" (
    echo.
    echo 正在生成 Anki 卡片...
    echo 需要依赖: genanki, edge-tts
    python generate_anki.py
    pause
    goto end
)

if "%choice%"=="7" (
    echo.
    echo 正在优化语言识别...
    python fix_language_detection.py
    pause
    goto end
)

if "%choice%"=="8" (
    echo.
    echo 正在启动本地服务器...
    echo 访问地址: http://localhost:8000
    echo.
    echo Dashboard:        http://localhost:8000/dashboard.html
    echo Semantic Search:  http://localhost:8000/semantic_search.html
    echo Index:            http://localhost:8000/index.html
    echo.
    echo 按 Ctrl+C 停止服务器
    python -m http.server 8000
    goto end
)

if "%choice%"=="0" (
    echo.
    echo 再见！
    goto end
)

echo.
echo ❌ 无效选项，请重新运行脚本
pause

:end
