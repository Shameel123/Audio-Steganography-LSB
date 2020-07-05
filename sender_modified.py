
import wave
import numpy as np
import matplotlib.pyplot as plt

song = wave.open("sin.wav", mode='rb')

frame_bytes = bytearray(list(song.readframes(song.getnframes())))


string="DSP Project on Audio Steganography using LSB Method."

x = np.linspace(0, 100, 100)
fig, axs = plt.subplots(2, 1, constrained_layout=True)
axs[0].plot(x, frame_bytes[0:100] , "-g")
axs[0].set_title('Original Wave')
axs[0].set_xlabel('Samples')
axs[0].set_ylabel('Amplitude')
fig.suptitle('Audio Wave Before & After Embedding Text Over 100 Samples', fontsize=16)

string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#' #adding redundant data

bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

try:
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
except IndexError:
    print("Please use a different .wav file with {} number of samples or use string with length of {}".format(len(string*8),int(len(frame_bytes)/8)))

axs[1].plot(x, frame_bytes[0:100] , "-b")
axs[1].set_xlabel('Samples')
axs[1].set_ylabel('Amplitude')
axs[1].set_title('Embedded Wave')
plt.show()

frame_modified = bytes(frame_bytes)

with wave.open('song_embedded.wav', 'wb') as fd:
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
song.close()
