import wave
import json
import vosk

# 使用解压后的模型的绝对路径
model_path = "/home/yang/mdk-T/catkin_ws/vosk-model-small-en-us-0.15"
model = vosk.Model(model_path)

def recognize_speech_from_wav(file_path):
    wf = wave.open(file_path, "rb")
    
    # 确保文件是符合要求的音频格式
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
        raise ValueError("音频格式不正确，需要 16kHz, 单声道, 16位音频")

    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    
    full_text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            full_text += " " + result['text']
        else:
            partial_result = json.loads(rec.PartialResult())
            print("Partial result:", partial_result['partial'])

    final_result = json.loads(rec.FinalResult())
    full_text += " " + final_result['text']

    return full_text.strip()

# 使用代码识别录音
file_path = './sound1.wav'

recognized_text = recognize_speech_from_wav(file_path)
print(f"Recognized text: {recognized_text}")