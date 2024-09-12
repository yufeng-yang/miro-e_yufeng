import scipy.signal
from scipy.io import wavfile
import numpy as np

def resample_audio(file_path, target_sample_rate=20000):
    # 读取原始音频文件
    sample_rate, data = wavfile.read(file_path)
    
    if sample_rate != target_sample_rate:
        # 计算新的采样数
        num_samples = int(len(data) * float(target_sample_rate) / sample_rate)
        data_resampled = scipy.signal.resample(data, num_samples)
        
        # 生成新的文件名
        new_file_path = file_path.replace(".wav", "_20kHz.wav")
        
        # 保存为新的WAV文件
        wavfile.write(new_file_path, target_sample_rate, data_resampled.astype(np.int16))
        print(f"Resampled audio saved as {new_file_path}")
        
        return new_file_path
    else:
        print("Sample rate is already 20kHz, no resampling needed.")
        return file_path
resample_audio('/home/miro/miro-e_yufeng/mdk-T/catkin_ws/sound1.wav')