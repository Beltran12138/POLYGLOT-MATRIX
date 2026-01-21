@echo off
chcp 65001 >nul
title Polyglot Matrix - 全流程更新

REM ==========================================
REM 🔄 一键完成：添加单词 → 生成卡片 → 部署
REM ==========================================

echo.
echo ========================================
echo   🔄 Polyglot Matrix - 全流程更新
echo ========================================
echo.
echo 本脚本将帮你完成:
echo   1. 解析新单词
echo   2. 合并到主数据库
echo   3. 生成 Anki 卡片 (可选)
echo   4. 部署到 GitHub (可选)
echo.

REM ==========================================
REM Step 1: 检查是否有新的 txt 文件
REM ==========================================
echo [1/4] 🔍 检查新单词文件...
set found_txt=0

for %%f in (*.txt) do (
    if not "%%f"=="nul" (
        set found_txt=1
        echo    找到: %%f
    )
)

if %found_txt%==0 (
    echo    ⚠️  没有找到 .txt 文件
    echo.
    set /p skip_parse="   跳过解析步骤? (y/n): "
    if /i "%skip_parse%"=="y" goto skip_parse
    echo.
    echo    💡 请先创建一个 .txt 文件，格式:
    echo       单词 词性.释义
    echo.
    pause
    exit /b
)

echo.
set /p do_parse="   是否解析这些文件? (y/n): "
if /i not "%do_parse%"=="y" goto skip_parse

echo.
echo ⚙️  正在解析单词...
python extract_vocab.py

if errorlevel 1 (
    echo.
    echo ❌ 解析失败！
    pause
    exit /b
)

echo.
echo ✅ 解析完成

:skip_parse

REM ==========================================
REM Step 2: 运行数据测试
REM ==========================================
echo.
echo [2/4] 🧪 测试数据完整性...
python test_data.py

if errorlevel 1 (
    echo.
    echo ⚠️  数据测试失败，请检查 vocabulary.json 格式
    pause
    exit /b
)

echo.
echo ✅ 数据验证通过

REM ==========================================
REM Step 3: 生成 Anki 卡片 (可选)
REM ==========================================
echo.
echo [3/4] 🎴 生成 Anki 卡片...
set /p do_anki="   是否生成 Anki 卡片? (y/n): "

if /i "%do_anki%"=="y" (
    echo.
    echo    ⚙️  正在生成 Anki 卡片...
    echo    ⚠️  这可能需要几分钟时间...
    python generate_anki.py

    if errorlevel 1 (
        echo.
        echo ⚠️  Anki 生成失败 (可能缺少依赖)
        echo    运行: pip install genanki edge-tts
    ) else (
        echo.
        echo ✅ Anki 卡片已生成
    )
) else (
    echo    ⏭️  已跳过 Anki 生成
)

REM ==========================================
REM Step 4: 部署到 GitHub (可选)
REM ==========================================
echo.
echo [4/4] 🚀 部署到 GitHub...
set /p do_deploy="   是否部署到 GitHub? (y/n): "

if /i "%do_deploy%"=="y" (
    echo.
    set /p commit_msg="   💬 提交信息 (直接回车使用默认): "

    if "%commit_msg%"=="" (
        set commit_msg=Update vocabulary and generated files
    )

    echo.
    echo    📦 部署中...
    call deploy.bat "%commit_msg%"

    if errorlevel 1 (
        echo.
        echo ❌ 部署失败
    ) else (
        echo.
        echo ✅ 部署成功
    )
) else (
    echo    ⏭️  已跳过部署
)

REM ==========================================
REM 完成
REM ==========================================
echo.
echo ========================================
echo   🎉 全流程更新完成！
echo ========================================
echo.
echo 💡 下一步建议:
echo    1. 刷新 dashboard.html 查看更新
echo    2. 打开 Anki 导入新卡片
echo    3. 访问在线版本查看效果
echo.

pause
