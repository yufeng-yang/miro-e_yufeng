import rospy
from std_msgs.msg import Int16MultiArray
import numpy as np
import json
import vosk

model_path = "/home/yang/mdk-T/catkin_ws/vosk-model-small-en-us-0.15"
model = vosk.Model(model_path)

def recognize_speech_from_data(audio_data, target_word):
    # 创建识别器，假设采样率为16kHz
    rec = vosk.KaldiRecognizer(model, 16000)
    
    found = False
    full_text = ""

    # 将音频数据分块输入识别器
    chunk_size = 4000  # 每次处理4000帧数据
    for i in range(0, len(audio_data), chunk_size):
        chunk = audio_data[i:i + chunk_size].tobytes()
        if rec.AcceptWaveform(chunk):
            result = json.loads(rec.Result())
            print("Intermediate result:", result['text'])
            full_text += " " + result['text']
            if target_word.lower() in result['text'].lower():
                found = True
        else:
            partial_result = json.loads(rec.PartialResult())
            print("Partial result:", partial_result['partial'])

    final_result = json.loads(rec.FinalResult())
    full_text += " " + final_result['text']
    print("Final result:", final_result['text'])
    if target_word.lower() in final_result['text'].lower():
        found = True

    if found:
        print(f"Detected '{target_word}' in the audio!")
        return True
    else:
        print(f"No '{target_word}' found in the audio.")
        return False

def callback(msg):
    # 将接收到的音频数据转换为numpy数组
    audio_data = np.array(msg.data, dtype=np.int16)
    rospy.loginfo("Received audio data, starting speech recognition...")

    # 调用语音识别函数
    target_word = "ball"
    recognize_speech_from_data(audio_data, target_word)

def audio_listener():
    rospy.init_node('audio_listener', anonymous=True)
    rospy.Subscriber("/miro/sensors/mics", Int16MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        audio_listener()
    except rospy.ROSInterruptException:
        pass