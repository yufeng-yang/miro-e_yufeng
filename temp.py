import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# 读取 wav 文件
file_path = './sound1.wav'
sample_rate, data = wavfile.read(file_path)

# 如果音频是多通道的，取其中一个通道
if len(data.shape) > 1:
    data = data[:, 0]

# 生成时间轴
time = np.linspace(0, len(data) / sample_rate, num=len(data))

# 绘制波形
plt.figure(figsize=(10, 6))
plt.plot(time, data)
plt.title('Audio Waveform')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()