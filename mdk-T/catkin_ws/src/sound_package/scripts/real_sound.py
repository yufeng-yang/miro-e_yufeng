import rospy
from std_msgs.msg import Int16MultiArray
import time
import numpy as np
import wave
import os

class Client:

    def play_wav_file(self, file_path):
        # 打开WAV文件
        try:
            wav_file = wave.open(file_path, 'rb')
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            return

        # 获取文件的参数
        num_channels = wav_file.getnchannels()  # 声道数
        sample_rate = wav_file.getframerate()   # 采样率
        num_frames = wav_file.getnframes()      # 总帧数

        # 打印音频信息
        print(f"Playing {file_path}, {num_frames} frames, {num_channels} channels at {sample_rate} Hz")

        # 读取音频数据
        audio_data = wav_file.readframes(num_frames)
        audio_data = np.frombuffer(audio_data, dtype=np.int16)  # 假设音频是 16 位

        wav_file.close()

        # 直接发布音频数据
        self.play_audio(audio_data, num_channels, sample_rate)

    def play_audio(self, audio_data, num_channels, sample_rate):
        chunk_size = 1024  # 每次发送的数据块大小
        time_per_chunk = chunk_size / sample_rate  # 计算每次发送数据块的延时

        print("Playing audio...")

        # 逐块发送音频数据
        for i in range(0, len(audio_data), chunk_size):
            chunk = audio_data[i:i+chunk_size]

            # 创建并发送消息
            msg = Int16MultiArray()
            msg.data = chunk.tolist()
            self.pub_stream.publish(msg)

            # 控制发送速率，确保音频按正确的速度播放
            time.sleep(time_per_chunk)

        print("Playback complete!")

    def __init__(self):
        # 初始化ROS节点
        rospy.init_node("client_audio_playback", anonymous=True)

        # 获取机器人名称
        topic_base_name = "/" + os.getenv("MIRO_ROBOT_NAME", "miro")

        # 发布音频流的主题
        topic = topic_base_name + "/control/stream"
        print("Publishing to", topic)
        self.pub_stream = rospy.Publisher(topic, Int16MultiArray, queue_size=10)

if __name__ == "__main__":
    # 创建客户端对象
    client = Client()

    # 提供要播放的WAV文件路径
    wav_file_path = "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/sound_package/scripts/sound1_20kHz.wav"

    # 播放音频文件
    client.play_wav_file(wav_file_path)
