import rospy
from std_msgs.msg import Int16MultiArray
import numpy as np

def publish_fake_audio():
    pub = rospy.Publisher('/miro/sensors/mics', Int16MultiArray, queue_size=10)
    rospy.init_node('fake_audio_publisher', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        # 生成模拟的音频数据，例如一个正弦波
        audio_data = (np.sin(2 * np.pi * np.linspace(0, 1, 16000)) * 32767).astype(np.int16)
        msg = Int16MultiArray(data=audio_data.tolist())

        rospy.loginfo("Publishing fake audio data")
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_fake_audio()
    except rospy.ROSInterruptException:
        pass
