#!/usr/bin/env python3
import rospy
import numpy as np
import sounddevice as sd
from std_msgs.msg import Int16MultiArray

class RealTimeAudioPlayer:
    def __init__(self):
        rospy.init_node('audio_listener', anonymous=True)
        
        # 设置采样率和缓冲大小
        self.sample_rate = 16000  # 根据实际情况设置
        self.num_channels = 4  # 话题中的通道数量
        self.samples_per_channel = 500  # 每个消息中的样本数量

        # 创建一个 ROS 订阅者
        rospy.Subscriber("/miro/sensors/mics", Int16MultiArray, self.callback)

    def callback(self, data):
        # 将接收到的多维数组转换为二维 numpy 数组，shape 为 (num_channels, samples_per_channel)
        audio_data = np.array(data.data).reshape((self.samples_per_channel, self.num_channels))

        # 对每个通道的数据进行归一化（可选）
        audio_data = audio_data / np.max(np.abs(audio_data))

        # 播放音频，每个通道的数据依次播放
        for i in range(self.num_channels):
            sd.play(audio_data[:, i], samplerate=self.sample_rate)
            sd.wait()  # 等待当前通道播放完成

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    player = RealTimeAudioPlayer()
    player.run()
