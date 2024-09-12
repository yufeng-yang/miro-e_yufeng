#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from std_msgs.msg import Bool

# 储存状态，是否检测到蓝色小球
ball_detected = False

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

                # 输出检测到的球的像素坐标（由外界打印，因此这里不用重复打印了）
                # rospy.loginfo(f"Detected ball at pixel coordinates: u={int(x)}, v={int(y)}")
                
                # 设置u, v为检测到的球的中心
                u, v = int(x), int(y)
                
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
    global right_image, ball_detected

    # 将ROS的Image消息转换为OpenCV图像
    left_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    
    # 调用图像处理模块中的检测函数
    u, v, detected_image = detect_blue_ball(left_image)
    if not ball_detected:
        if u is not None and v is not None:
            rospy.loginfo(f"Ball detected at coordinates u={u}, v={v}")
            ball_detected = True
            print(ball_detected)
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

############################################

#!/usr/bin/env python3
# import rospy
# from sensor_msgs.msg import Image
# from std_msgs.msg import Bool
# from cv_bridge import CvBridge
# import cv2
# import numpy as np

# # 标志位，用于跟踪是否检测到球体
# ball_detected = False
# trigger_detection = False  # 通过语音识别触发的检测标志

# # 创建一个发布者
# stop_pub = rospy.Publisher('/miro/control/stop_rotation', Bool, queue_size=10)

# def detect_blue_ball(image):
#     global ball_detected

#     # 如果已经检测到球体，直接返回
#     if ball_detected:
#         return None, None, image

#     # 检测逻辑
#     hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     lower_blue = np.array([100, 150, 50])
#     upper_blue = np.array([140, 255, 255])
#     mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
#     kernel = np.ones((3, 3), np.uint8)
#     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#     mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     u, v = None, None
#     for contour in contours:
#         if len(contour) >= 5:
#             ellipse = cv2.fitEllipse(contour)
#             (x, y), (MA, ma), angle = ellipse
#             aspect_ratio = ma / MA
#             if 0.8 < aspect_ratio < 1.2:
#                 cv2.ellipse(image, ellipse, (0, 255, 0), 2)
#                 u, v = int(x), int(y)
#                 ball_detected = True  # 设置标志，避免重复检测
#                 rospy.loginfo(f"Ball detected at coordinates u={u}, v={v}")
#                 stop_pub.publish(True)  # 发布停止命令
#                 break

#     return u, v, image

# def trigger_callback(msg):
#     global trigger_detection
#     if msg.data:
#         rospy.loginfo("Trigger signal received, starting ball detection.")
#         trigger_detection = True  # 当收到触发信号时，开始检测

# def left_image_callback(msg):
#     global trigger_detection

#     if trigger_detection:  # 只有在触发检测后才进行处理
#         left_image = bridge.imgmsg_to_cv2(msg, "bgr8")
#         u, v, detected_image = detect_blue_ball(left_image)
#         cv2.imshow("Camera Image", detected_image)
#         cv2.waitKey(1)

# def main():
#     global bridge
#     rospy.init_node('ball_detection_node')

#     bridge = CvBridge()

#     # 订阅触发信号
#     rospy.Subscriber('/trigger_image_processing', Bool, trigger_callback)

#     # 订阅摄像头图像
#     rospy.Subscriber('/miro/sensors/caml', Image, left_image_callback)

#     rospy.spin()
#     cv2.destroyAllWindows()

if __name__ == '__main__':
    main()


