import sounddevice as sd 
from scipy.io.wavfile import write
import numpy as np

freq = 44100
duration=10
print("speak")

recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
sd.wait()

# before saving make all integers in array 32 bit      
y = (np.iinfo(np.int32).max * (recording/np.abs(recording).max())).astype(np.int32)
write("recording0.wav", freq, y)

print("successfully recorded") 