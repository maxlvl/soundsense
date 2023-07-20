import wave
import numpy as np
import matplotlib

# Hack to switch matplotlib to a GUI supported backend. Need to do it here as you can't switch backends once you've initialized matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt

wav_object = wave.open("source_audio/1_laugh.wav", "rb")

sample_frequency = wav_object.getframerate()
# num_channels = wav_object.getnchannels()

num_samples = wav_object.getnframes()
signal_wave = wav_object.readframes(num_samples)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

l_channel = signal_array[0::2]
r_channel = signal_array[1::2]

times = np.linspace(0, num_samples / sample_frequency, num=num_samples)
total_audio = num_samples / sample_frequency

# Plotting
plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title("Left Channel")
plt.ylabel("Signal Value")
plt.xlabel("Time in seconds")
plt.xlim(0, total_audio)
plt.show()
