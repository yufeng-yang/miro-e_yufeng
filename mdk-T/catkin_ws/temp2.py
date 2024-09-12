import wave
import json
import vosk

model_path = "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/vosk-model-small-en-us-0.15"

model = vosk.Model(model_path)

def recognize_speech_from_wav(file_path, target_word):
    wf = wave.open(file_path, "rb")
    
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
        raise ValueError("别忘记用ffmpeg -i sound1.wav -ar 16000 -ac 1 -f wav sound1.wav, 转成16kHz, 单声道, 16位音频")

    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    
    found = False
    full_text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
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

# 使用代码识别录音
file_path = '/tmp/test1.wav'
target_word = "ball"

if recognize_speech_from_wav(file_path, target_word):
    print("Trigger the desired action.")
else:
    print(f"No '{target_word}' found in the audio.")
