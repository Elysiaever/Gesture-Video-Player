@echo off
REM 创建虚拟环境
echo [1/4] 正在创建虚拟环境 myvenv ...
python -m venv myvenv

REM 激活虚拟环境
echo [2/4] 正在激活虚拟环境 ...
call myvenv\Scripts\activate

REM 安装依赖
echo [3/4] 正在安装依赖 ...
pip install --upgrade pip
pip install -r requirements.txt

REM 启动 Flask 项目
echo [4/4] 正在启动 Flask 项目 ...
python app.py

pause
