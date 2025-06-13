# ========== services/gesture_model.py ==========
import torch
from torchvision import transforms
from ultralytics.nn.tasks import DetectionModel
from PIL import Image

# 允许安全加载 DetectionModel
torch.serialization.add_safe_globals([DetectionModel])

# 加载模型（根据实际模型路径调整）
model = torch.load('gesture_model.pt', map_location=torch.device('cpu'),weights_only=False)
model.eval()

# 定义图像预处理流程
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict_gesture(image_file):
    """对上传图像执行推理，返回手势编号或标签"""
    image = Image.open(image_file).convert('RGB')
    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(input_tensor)
        predicted = torch.argmax(output, dim=1).item()

    return str(predicted)

