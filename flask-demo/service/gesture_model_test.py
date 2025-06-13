# ========== services/gesture_model.py ==========
# import torch  # 暂时不用真实模型
# from torchvision import transforms
from PIL import Image
import random  # 用于随机生成手势编号

# 模拟模型逻辑：暂不加载真实模型，返回随机结果或固定值

# def transform = ... 也不需要图像预处理流程

def predict_gesture(image_file):
    """
    模拟对上传图像执行推理，返回一个手势编号
    （后期可替换为真实模型逻辑）
    """
    image = Image.open(image_file).convert('RGB')  # 模拟打开图像

    # 固定返回值（可选）
    # return "0"  # 总是返回播放手势

    # 或者返回 0~5 的随机手势编号
    return str(random.randint(0, 5))
