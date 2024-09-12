#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import TwistStamped
from std_msgs.msg import Bool 

# 初始化ROS节点
rospy.init_node("circle_motion")

# 创建一个发布者
cm_pub = rospy.Publisher("/miro/control/cmd_vel", TwistStamped, queue_size=10)

rate = rospy.Rate(10)
twistS = TwistStamped()

# 标志变量，控制是否停止旋转
stop_rotation = False

def stop_callback(msg):
    global stop_rotation
    if msg.data:  # 如果接收到True，则停止旋转
        stop_rotation = True

# 订阅停止命令的话题
rospy.Subscriber("/miro/control/stop_rotation", Bool, stop_callback)

while not rospy.is_shutdown():
    if stop_rotation:
        # 停止运动
        twistS.twist.linear.x = 0.0
        twistS.twist.linear.y = 0.0
        twistS.twist.linear.z = 0.0
        
        twistS.twist.angular.x = 0.0
        twistS.twist.angular.y = 0.0
        twistS.twist.angular.z = 0.0
        rospy.loginfo("Ball found, stopping rotation.")
    else:
        # 继续旋转
        twistS.twist.angular.z = 0.5
        twistS.twist.linear.x = -0.1  # 保持旋转速度

    # 发布消息
    cm_pub.publish(twistS)
    
    # 等待下一个循环
    rate.sleep()


