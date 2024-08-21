#! /usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
# from ellipse_reco import detect_blue_ball
from ellipse_reco import detect_blue_ball
from distance import calculate_distance

# 初始化节点
rospy.init_node("zuoYan")

# 创建CvBridge对象
bridge = CvBridge()

# 用于存储右摄像头图像
right_image = None

def left_image_callback(msg):
    global right_image

    # 将ROS的Image消息转换为OpenCV图像
    left_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    
    # 调用图像处理模块中的检测函数
    u, v, detected_image = detect_blue_ball(left_image)
    
    if u is not None and v is not None:
        rospy.loginfo(f"Ball detected at coordinates u={u}, v={v}")

        if right_image is not None:
            try:
                # 计算三维坐标
                X, Y, Z = calculate_distance(left_image, right_image, u, v)
                rospy.loginfo(f"Ball's 3D coordinates: X={X:.2f}, Y={Y:.2f}, Z={Z:.2f}")
            except ValueError as e:
                rospy.logwarn(str(e))
    
    # 显示图像
    cv2.imshow("Camera Image", detected_image)
    cv2.waitKey(1)  # 必须加上这一行，否则图像窗口不会刷新

def right_image_callback(msg):
    global right_image
    right_image = bridge.imgmsg_to_cv2(msg, "bgr8")

# 订阅左、右摄像头的话题
left_image_sub = rospy.Subscriber('/miro/sensors/caml', Image, left_image_callback)
right_image_sub = rospy.Subscriber('/miro/sensors/camr', Image, right_image_callback)

# 保持节点运行
rospy.spin()

cv2.destroyAllWindows()

# import rospy
# from sensor_msgs.msg import Image
# from std_msgs.msg import Bool
# from cv_bridge import CvBridge
# import cv2
# from ellipse_reco import detect_blue_ball
# from distance import calculate_distance

# # 初始化节点
# rospy.init_node("zuoYan")

# bridge = CvBridge()
# right_image = None

# def left_image_callback(msg):
#     global right_image

#     left_image = bridge.imgmsg_to_cv2(msg, "bgr8")
#     u, v, detected_image = detect_blue_ball(left_image)

#     if u is not None and v is not None:
#         rospy.loginfo(f"Ball detected at coordinates u={u}, v={v}")
#         if right_image is not None:
#             try:
#                 X, Y, Z = calculate_distance(left_image, right_image, u, v)
#                 rospy.loginfo(f"Ball's 3D coordinates: X={X:.2f}, Y={Y:.2f}, Z={Z:.2f}")
#             except ValueError as e:
#                 rospy.logwarn(str(e))

#     cv2.imshow("Camera Image", detected_image)
#     cv2.waitKey(1)

# def right_image_callback(msg):
#     global right_image
#     right_image = bridge.imgmsg_to_cv2(msg, "bgr8")

# def trigger_callback(msg):
#     if msg.data:
#         rospy.loginfo("Trigger signal received, starting image processing.")
#         left_image_sub = rospy.Subscriber('/miro/sensors/caml', Image, left_image_callback)
#         right_image_sub = rospy.Subscriber('/miro/sensors/camr', Image, right_image_callback)

# trigger_sub = rospy.Subscriber('/trigger_image_processing', Bool, trigger_callback)
# rospy.spin()

# cv2.destroyAllWindows()
