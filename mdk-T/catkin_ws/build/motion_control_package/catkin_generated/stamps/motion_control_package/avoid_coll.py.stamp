import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import TwistStamped
import time

class SimpleObstacleAvoidance:
    def __init__(self):
        # 初始化ROS节点
        rospy.init_node('simple_obstacle_avoidance', anonymous=True)

        # 订阅传感器数据
        rospy.Subscriber('/miro/sensors/sonar', Range, self.sensor_callback)

        # 发布速度控制命令
        self.cmd_vel_pub = rospy.Publisher('/miro/control/cmd_vel', TwistStamped, queue_size=10)

        # 初始化速度指令
        self.move_cmd = TwistStamped()
        self.safe_distance = 0.1
        self.obstacle_detected = False

        # 初始化声纳距离
        self.current_distance = 0.0

        # 初始化计时器，用于控制控制台输出的频率
        self.last_print_time = time.time()

    def sensor_callback(self, data):
        # 更新当前的距离
        self.current_distance = data.range

        # 如果检测到距离小于安全距离，则认为有障碍物
        if self.current_distance < self.safe_distance:
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False

    def run(self):
        rate = rospy.Rate(10)  # 10 Hz
        while not rospy.is_shutdown():
            current_time = time.time()
            if current_time - self.last_print_time >= 0.5:  # 每0.5秒打印一次
                rospy.loginfo(f"Sonar Distance: {self.current_distance:.2f} meters")
                self.last_print_time = current_time

            if self.obstacle_detected:
                rospy.loginfo("Obstacle detected! Turning...")
                # 如果检测到障碍物，停止前进并转向
                self.move_cmd.twist.linear.x = 0.0
                self.move_cmd.twist.linear.y = 0.0
                self.move_cmd.twist.linear.z = 0.0

                self.move_cmd.twist.angular.x = 0.0
                self.move_cmd.twist.angular.y = 0.0
                self.move_cmd.twist.angular.z = 0.5  # 向右转弯
            else:
                rospy.loginfo("No obstacle. Moving forward...")
                # 向前移动
                self.move_cmd.twist.linear.x = 0.2
                self.move_cmd.twist.linear.y = 0.0
                self.move_cmd.twist.linear.z = 0.0

                self.move_cmd.twist.angular.x = 0.0
                self.move_cmd.twist.angular.y = 0.0
                self.move_cmd.twist.angular.z = 0.0

            # 发布速度指令
            self.cmd_vel_pub.publish(self.move_cmd)
            rate.sleep()

if __name__ == '__main__':
    try:
        node = SimpleObstacleAvoidance()
        node.run()
    except rospy.ROSInterruptException:
        pass
