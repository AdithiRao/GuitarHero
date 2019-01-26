import module_manager
module_manager.review()
import pyaudio
import wave
import time
import aubio

open_wave = wave.open("Yamaha-V50-Synbass-1-C2.wav",'rb')

pyAudio_session = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    data = open_wave.readframes(frame_count)
    return (data, pyaudio.paContinue)

pyAudio_stream = pyAudio_session.open(
    format = pyAudio_session.get_format_from_width(open_wave.getsampwidth()),
    channels = open_wave.getnchannels(),
    rate = open_wave.getframerate(),
    output = True,
    stream_callback=callback)

while pyAudio_stream.is_active():
    time.sleep(0.1)

pyAudio_stream.stop_stream()
pyAudio_stream.close()
print("Stopped")
pyAudio_session.terminate()
