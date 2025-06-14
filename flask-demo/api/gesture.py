# api/gesture.py
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from service.gesture_model import predict_gesture

gesture_bp = Blueprint('gesture', __name__)

@gesture_bp.route('/predict', methods=['POST'])
@swag_from({
    'tags': ['Gesture'],
    'summary': '手势识别',
    'consumes': ['multipart/form-data'],
    'parameters': [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': '上传一张包含手势的图片'
        }
    ],
    'responses': {
        200: {
            'description': '识别成功',
            'examples': {
                'application/json': {
                    'gesture': 'stop'
                }
            }
        },
        400: {
            'description': '请求错误，例如缺少文件'
        }
    }
})
def predict():
    """
    上传图像进行手势识别
    """
    if 'file' not in request.files:
        return jsonify({'error': '缺少文件'}), 400

    file = request.files['file']
    try:
        gesture = predict_gesture(file)
        return jsonify({'gesture': gesture})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
