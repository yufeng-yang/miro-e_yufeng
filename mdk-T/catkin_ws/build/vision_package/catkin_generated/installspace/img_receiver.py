#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

# 初始化节点
rospy.init_node("zuoYan")

# 创建CvBridge对象
bridge = CvBridge()

def left_image_callback(msg):
    # 将ROS的Image消息转换为OpenCV图像
    left_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    
    # 显示图像
    cv2.imshow("Left Camera Image", left_image)
    cv2.waitKey(1)  # 必须加上这一行，否则图像窗口不会刷新

# 订阅左眼摄像头的话题
left_image_sub = rospy.Subscriber('/miro/sensors/caml', Image, left_image_callback)

# 保持节点运行
rospy.spin()

cv2.destroyAllWindows()

