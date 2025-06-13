# ========== api/gesture.py ==========
from flask import Blueprint, request, jsonify
from flasgger import swag_from

from service.gesture_model_test import predict_gesture
from utils.gesture_map import gesture_to_command
gesture_bp = Blueprint('gesture', __name__)

@gesture_bp.route('/recognize', methods=['POST'])
@swag_from({
    'tags': ['Gesture Recognition'],
    'summary': '上传图片识别手势',
    'consumes': ['multipart/form-data'],
    'parameters': [
        {
            'name': 'image',
            'in': 'formData',
            'type': 'file',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': '返回识别结果和命令',
            'examples': {
                'application/json': {'gesture': '1', 'command': 'pause'}
            }
        }
    }
})
def recognize():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    gesture = predict_gesture(image)
    command = gesture_to_command(gesture)
 #   gesture = '1'  # 假设测试手势为 "1"
  #  command = 'pause'

    return jsonify({
        'gesture': gesture,
        'command': command
    })
