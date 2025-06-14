# gesture_model.py

from ultralytics import YOLO
import numpy as np
from PIL import Image

# 加载模型（只加载一次）
model = YOLO("models/gesture_model.pt")  # 替换为你的模型路径

# 类别标签映射（根据你模型实际输出调整）
gesture_labels = {
    0: "grabbing", 1: "grip", 2: "holy", 3: "point", 4: "take_photo",
    5: "three3", 6: "timeout", 7: "xsign", 8: "heart2", 9: "heart",
    10: "pinkie", 11: "mid_finger", 12: "call", 13: "dislike",
    14: "fist", 15: "four", 16: "like", 17: "mute", 18: "ok", 19: "one",
    20: "palm", 21: "peace", 22: "peace_inv.", 23: "rock",
    24: "stop", 25: "stop_inv.", 26: "three", 27: "three2",
    28: "two_up", 29: "two_up_inv.", 30: "gun", 31: "thumb_index",
    32: "thumb_index2", 33: "no_gesture"
}

# 颜色映射（与标签对应）
colors = {
    0: (255, 0, 0),  # grabbing - 红色
    1: (0, 255, 0),  # grip - 绿色
    2: (0, 0, 255),  # holy - 蓝色
    24: (200, 0, 200),  # stop - 深紫色（用于暂停控制）
    18: (128, 255, 128),  # ok - 浅绿色（用于播放控制）
    3: (255, 255, 0),  # point - 黄色（用于快进）
    2: (0, 0, 255),  # holy - 蓝色（用于快退）
    # 其他颜色...
}

def predict_gesture(file, conf_threshold=0.5):
    """
    使用 YOLO 模型检测上传图像中的手势。

    参数：
        file: 上传的图像文件（file.stream）
        conf_threshold: 置信度阈值

    返回：
        若检测到手势：dict(gesture, confidence, box)
        否则：None
    """
    image = Image.open(file.stream).convert("RGB")
    image_np = np.array(image)
    results = model(image_np)

    for result in results:
        for box in result.boxes:
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            if conf > conf_threshold:
                return {
                    "gesture": gesture_labels.get(cls, f"class_{cls}"),
                    "confidence": round(conf, 3),
                    "box": list(map(int, box.xyxy[0]))
                }

    return None
