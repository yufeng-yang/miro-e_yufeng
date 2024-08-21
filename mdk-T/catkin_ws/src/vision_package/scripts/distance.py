import cv2
import numpy as np

def calculate_distance(left_image, right_image, u, v):
    # 将图像转换为灰度
    gray_left = cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)
    
    # 立体匹配器
    stereo_matcher = cv2.StereoBM_create(numDisparities=16*5, blockSize=15)
    
    # 计算视差图
    disparity = stereo_matcher.compute(gray_left, gray_right).astype(np.float32) / 16.0
    
    # 获取视差值
    d = disparity[int(v), int(u)]
    
    if d > 0:  # 确保视差值有效
        # 相机内参（使用之前推导的值）
        fx = 700  # 这个值需要根据你的相机标定实际调整
        BASELINE = 0.0862  # 基线距离，以米为单位
        
        # 计算深度 Z
        Z = (fx * BASELINE) / d
        
        # 计算三维坐标 X, Y
        cx, cy = 640 / 2, 480 / 2  # 假设图像的中心点
        X = (u - cx) * Z / fx
        Y = (v - cy) * Z / fx
        
        return X, Y, Z
    else:
        raise ValueError("Invalid disparity value. Unable to calculate depth.")