@echo off
REM 激活虚拟环境（确保路径正确）
call myvenv\Scripts\activate

REM 设置 Flask 环境变量（可选，方便调试）
set FLASK_APP=app.py
set FLASK_ENV=development

REM 启动 Flask 应用
python app.py

pause
