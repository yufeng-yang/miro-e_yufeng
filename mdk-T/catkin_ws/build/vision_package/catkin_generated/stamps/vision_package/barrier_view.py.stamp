#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from std_msgs.msg import Bool

# 储存状态，是否检测到红色长方形
rectangle_detected = False

# 创建一个发布者（全局范围内）
stop_pub = rospy.Publisher('/miro/control/stop_rotation', Bool, queue_size=10)

def detect_red_rectangle(image):
    # 将图像从BGR转换为HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义红色的颜色范围
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # 创建两个掩模，保留颜色范围内的区域
    mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    mask = mask1 | mask2

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
            # 拟合多边形
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # 如果多边形有四个顶点，则认为是矩形
            if len(approx) == 4:
                # 检查是否为接近长方形的形状
                (x, y, w, h) = cv2.boundingRect(approx)
                aspect_ratio = float(w) / h
                
                if 0.5 < aspect_ratio < 2.0:  # 宽高比适合长方形
                    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
                    cv2.putText(image, "Red Rectangle Detected", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (36, 255, 12), 2)

                    # 设置u, v为检测到的长方形的中心
                    u, v = int(x + w / 2), int(y + h / 2)
                    
                    # 发布停止命令
                    stop_pub.publish(True)
                    break  # 停止检测，避免重复发出停止命令

    return u, v, image

# 初始化节点
rospy.init_node("zuoYan")

# 创建CvBridge对象
bridge = CvBridge()

# 用于存储右摄像头图像
right_image = None

def left_image_callback(msg):
    global right_image, rectangle_detected

    # 将ROS的Image消息转换为OpenCV图像
    left_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    
    # 调用图像处理模块中的检测函数
    u, v, detected_image = detect_red_rectangle(left_image)
    if not rectangle_detected:
        if u is not None and v is not None:
            rospy.loginfo(f"Rectangle detected at coordinates u={u}, v={v}")
            rectangle_detected = True
            print(rectangle_detected)
            # 更新标志，确保只打印一次

    # 显示图像
    cv2.imshow("Camera Image", detected_image)
    cv2.waitKey(1)  # 必须加上这一行，否则图像窗口不会刷新

# 订阅左、右摄像头的话题
left_image_sub = rospy.Subscriber('/miro/sensors/caml', Image, left_image_callback)
right_image_sub = rospy.Subscriber('/miro/sensors/camr', Image, lambda msg: None)  # 保持right_image_callback，但暂时不使用

# 保持节点运行
rospy.spin()

cv2.destroyAllWindows()
