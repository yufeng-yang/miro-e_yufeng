import numpy as np
from scipy.io.wavfile import write

def generate_sine_wave(frequency, duration, sample_rate=44100, amplitude=0.5):
    """
    生成正弦波音频。
    
    参数:
    frequency: 正弦波频率 (Hz)
    duration: 音频时长 (秒)
    sample_rate: 采样率 (默认 44100 Hz)
    amplitude: 振幅 (0.0 到 1.0)

    返回:
    numpy 数组表示的音频数据
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # 时间点
    audio_data = amplitude * np.sin(2 * np.pi * frequency * t)  # 正弦波
    return audio_data

# 生成1秒钟的440Hz（A4音符）的正弦波
audio_data = generate_sine_wave(440, 1)

# 将音频数据缩放到16位整数（WAV文件格式）
scaled = np.int16(audio_data * 32767)

# 保存为WAV文件
write("test_sine_wave.wav", 44100, scaled)
