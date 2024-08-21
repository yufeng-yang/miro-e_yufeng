#! /usr/bin/env python3
import cv2
import numpy as np
import rospy
from std_msgs.msg import Bool  # 使用布尔类型消息

# 创建一个发布者（全局范围内）
stop_pub = rospy.Publisher('/miro/control/stop_rotation', Bool, queue_size=10)

def detect_blue_ball(image):
    # 将图像从BGR转换为HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义蓝色的颜色范围
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    # 创建一个掩模，保留颜色范围内的区域
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # 使用形态学操作去除噪声
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # 显示掩模图像
    cv2.imshow("Mask", mask)

    # 寻找轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    u, v = None, None
    for contour in contours:
        # 如果轮廓足够大
        if len(contour) >= 5:
            # 拟合椭圆
            ellipse = cv2.fitEllipse(contour)
            (x, y), (MA, ma), angle = ellipse
            aspect_ratio = ma / MA
            
            # 可以根据实际需求设置椭圆的长宽比范围
            if 0.8 < aspect_ratio < 1.2:  # 接近正圆的椭圆
                cv2.ellipse(image, ellipse, (0, 255, 0), 2)
                cv2.putText(image, "Blue Ball Detected", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (36, 255, 12), 2)

                # 输出检测到的球的像素坐标
                rospy.loginfo(f"Detected ball at pixel coordinates: u={int(x)}, v={int(y)}")
                
                # 设置u, v为检测到的球的中心
                u, v = int(x), int(y)
                
                # 发布停止命令
                stop_pub.publish(True)
                break  # 停止检测，避免重复发出停止命令

    return u, v, image