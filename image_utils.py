import cv2 
import numpy as np
import os
def load_image_robust(image_path):
    """
    安全读取图像，支持中文路径，失败时给出明确错误原因。
    返回: (图像BGR数组, 是否成功)
    """
    # 1. 检查路径是否为字符串
    if not isinstance(image_path, str):
        print("错误: 路径必须是字符串。")
        return None, False

    # 2. 检查文件是否存在
    if not os.path.exists(image_path):
        print(f"错误: 文件不存在 -> {image_path}")
        return None, False

    # 3. 使用 imdecode 读取（完美支持中文路径）
    try:
        img_array = np.fromfile(image_path, dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)  # -1 代表原色加载
    except Exception as e:
        print(f"读取文件时异常: {e}")
        return None, False

    # 4. 检查解码是否成功
    if img is None:
        print(f"错误: 无法解码图像，可能是格式损坏或不支持 -> {image_path}")
        return None, False

    print("✅ 图像读取成功！")
    return img, True