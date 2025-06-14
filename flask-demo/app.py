# app.py
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
CORS(app)

# Swagger 配置
Swagger(app)

# 注册蓝图
from api.video import video_bp
from api.gesture import gesture_bp

app.register_blueprint(video_bp, url_prefix='/api/video')
app.register_blueprint(gesture_bp, url_prefix='/api/gesture')

if __name__ == '__main__':
    app.run(debug=True)
