import rospy
from std_msgs.msg import Int16MultiArray
from scipy.io import wavfile
import numpy as np

def publish_fake_audio():
    pub = rospy.Publisher('/miro/sensors/mics', Int16MultiArray, queue_size=10)
    rospy.init_node('fake_audio_publisher', anonymous=True)

    # 读取 sound1.wav 文件
    file_path = '/home/miro/miro-e_yufeng/mdk-T/catkin_ws/sound1.wav'  # 请确保路径正确
    sample_rate, audio_data = wavfile.read(file_path)

    # 确保音频数据为 int16 类型
    audio_data = audio_data.astype(np.int16)

    # 发布一次音频数据
    msg = Int16MultiArray(data=audio_data.tolist())
    rospy.loginfo("Publishing fake audio data")
    pub.publish(msg)

    # 让节点保持活动状态以确保消息发送
    rospy.spin()

if __name__ == '__main__':
    try:
        publish_fake_audio()
    except rospy.ROSInterruptException:
        pass