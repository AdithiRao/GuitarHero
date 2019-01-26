import pyaudio
import wave
import scipy.io.wavfile as wavfile
import numpy as np
from matplotlib import pylab
import pylab as pl
import math
import time
# from pydub import AudioSegment

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 512
WAVE_OUTPUT_FILENAME = "recordedFile.wav"
device_index = 2
audio = pyaudio.PyAudio()

# Hardcoding for Vaishnavi's Inputs to Built-in-Microphone which corresponds to index 0
# print("----------------------record device list---------------------")
# info = audio.get_host_api_info_by_index(0)
# numdevices = info.get('deviceCount')
# for i in range(0, numdevices):
#         if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
#             print ( "Input Device id ", i, " - ", audio.get_device_info_by_host_api_device_index(0, i).get('name'))

# print("-------------------------------------------------------------")

# index = int(input())

RECORD_SECONDS = 3  # default


index = 0
print("recording via index "+str(index))

stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,input_device_index = index,
                frames_per_buffer=CHUNK)
print ("recording started")
Recordframes = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    Recordframes.append(data)
print ("recording stopped")


stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(Recordframes))
waveFile.close()


open_wave = wave.open("recordedFile.wav",'rb')

pyAudio_session = pyaudio.PyAudio()
rate, data = wavfile.read("recordedFile.wav")

def callback(in_data, frame_count, time_info, status):
    data = open_wave.readframes(frame_count)
    return (data, pyaudio.paContinue)

pyAudio_stream = pyAudio_session.open(
    format = pyAudio_session.get_format_from_width(open_wave.getsampwidth()),
    channels = open_wave.getnchannels(),
    rate = open_wave.getframerate(),
    output = True,
    stream_callback=callback)

# for i in range(len(data)):
#     print(data[i])

print(rate)
print(len(data))

i=0
while pyAudio_stream.is_active():
    i+=1
    #time.sleep(0.1)

print(len(data)/i)
newVar = len(data)/i
j = 0
while pyAudio_stream.is_active():
    print(data + j*newVar)
    j+=1

pyAudio_stream.stop_stream()
pyAudio_stream.close()
print("Stopped")
pyAudio_session.terminate()






# newData = []
# rate, data = wavfile.read("Yamaha-V50-Synbass-1-C2.wav")
# print(len(data))
# for i in range(len(data)):
#
#     # data[i][0] = math.sin(data[i][0])
#     #print data[i][0]
#
#
# t = np.arange(len(data[:,0]))*1.0/rate
# pl.plot(t, data[:,0])
# pl.show()
