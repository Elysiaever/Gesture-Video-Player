# app.py
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
CORS(app)

# Swagger 配置
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "swagger_ui": True,
    "specs_route": "/docs/"
}
Swagger(app, config=swagger_config)

# 注册蓝图
from api.video import video_bp
from api.gesture import gesture_bp

app.register_blueprint(video_bp, url_prefix='/api/video')
app.register_blueprint(gesture_bp, url_prefix='/api/gesture')

if __name__ == '__main__':
    app.run(debug=True)
