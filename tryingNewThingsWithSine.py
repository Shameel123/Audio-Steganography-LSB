
import matplotlib.pyplot as plt

import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

x = np.linspace(0, 900000000000000000000000000000000000,480000)

# frequency is the number of times a wave repeats a second
frequency = 1000
num_samples = 480000
# The sampling rate of the analog to digital convert
sampling_rate = 480000
amplitude = 16
file = "sin.wav"
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]
# sine_wave = sine_wave + sine_wave
plt.plot(x , sine_wave, "-g", label="sine")
plt.show()
nframes=num_samples

comptype="NONE"

compname="not compressed"

nchannels=1

sampwidth=2

wav_file=wave.open(file, 'w')

wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

print(nframes)

for s in sine_wave:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))

struct.pack('h', int(s*amplitude))
int(s*amplitude)
