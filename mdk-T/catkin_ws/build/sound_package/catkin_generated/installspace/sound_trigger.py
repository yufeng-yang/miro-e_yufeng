import rospy
from std_msgs.msg import Int16MultiArray, Bool
import numpy as np
import json
import vosk

model_path = "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/vosk-model-small-en-us-0.15"
model = vosk.Model(model_path)

def recognize_speech_from_data(audio_data, target_word):
    rec = vosk.KaldiRecognizer(model, 16000)
    found = False
    full_text = ""

    chunk_size = 4000
    rospy.loginfo("Starting speech recognition...")

    for i in range(0, len(audio_data), chunk_size):
        chunk = audio_data[i:i + chunk_size].tobytes()
        if rec.AcceptWaveform(chunk):
            result = json.loads(rec.Result())
            rospy.loginfo(f"Intermediate result: {result['text']}")
            full_text += " " + result['text']
            if target_word.lower() in result['text'].lower():
                found = True
        else:
            partial_result = json.loads(rec.PartialResult())
            rospy.loginfo(f"Partial result: {partial_result['partial']}")

    final_result = json.loads(rec.FinalResult())
    full_text += " " + final_result['text']
    rospy.loginfo(f"Final result: {final_result['text']}")

    if target_word.lower() in final_result['text'].lower():
        found = True

    if found:
        rospy.loginfo(f"Detected '{target_word}' in the audio!")
        trigger_pub.publish(True)
    else:
        rospy.loginfo(f"No '{target_word}' found in the audio.")

def callback(msg):
    audio_data = np.array(msg.data, dtype=np.int16)
    rospy.loginfo("Received audio data, starting speech recognition...")
    target_word = "ball"
    recognize_speech_from_data(audio_data, target_word)

def audio_listener():
    global trigger_pub
    rospy.init_node('audio_listener', anonymous=True)
    rospy.Subscriber("/miro/sensors/mics", Int16MultiArray, callback)
    trigger_pub = rospy.Publisher('/trigger_image_processing', Bool, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    try:
        audio_listener()
    except rospy.ROSInterruptException:
        pass


