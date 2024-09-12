import rospy
import numpy as np
import json
from vosk import Model, KaldiRecognizer
from std_msgs.msg import Int16MultiArray

class RobotAudioRecognition:
    def __init__(self):
        rospy.init_node('robot_audio_recognition', anonymous=True)

        model_path = "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/vosk-model-small-en-us-0.15"
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)

        rospy.Subscriber("/miro/sensors/mics", Int16MultiArray, self.audio_callback)
        rospy.loginfo("Robot audio recognition node started")

    def audio_callback(self, data):
        audio_data = np.array(data.data, dtype=np.int16)

        # 假设第一通道（Left Ear）是主要语音通道
        audio_channel_data = audio_data[::4]  # 选择第一个通道的音频数据

        audio_bytes = audio_channel_data.tobytes()

        if self.recognizer.AcceptWaveform(audio_bytes):
            result = self.recognizer.Result()
            text = json.loads(result).get("text", "")
            if text:
                rospy.loginfo(f"Recognized Speech: {text}")

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = RobotAudioRecognition()
    node.run()
