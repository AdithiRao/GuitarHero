# Records for desired number of seconds and plays recorded song

import pyaudio
import wave


def record(seconds):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 512
    WAVE_OUTPUT_FILENAME = "recordedFile2.wav"
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
    index = 0

    RECORD_SECONDS = seconds  # default
    # duration = input("Enter duration of song in m:s format: \n")
    # (m,s) = duration.split(":")
    # RECORD_SECONDS = (int(m)*60) + int(s)

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



#
