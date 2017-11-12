import pyaudio
import numpy as np
from random import randint

class pyAudio(object):

    def __init__(self,val):
        self.freq = 0
        for k in val:
            self.freq = k
            self.generateAudio(self.freq)
    def generateAudio(self,val):
        
        p = pyaudio.PyAudio()

        volume = 0.5     # range [0.0, 1.0]
        fs =   44100       # sampling rate, Hz, must be integer
        #100000 sampling rate is cool and good sound using one channeles.
        duration = 2   # in seconds, may be float
        f = 440.0 - val*40       # sine frequency, Hz, may be float
        print(str(f))
        # generate samples, note conversion to float32 array
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)
        #Helicopter sound for channels value 30 and it can't exceed that value.
        #for channels 5 and duration 6,you will be getting dial tone sound.

        # play. May repeat with different volume values (if done interactively) 
        stream.write(volume*samples)

        stream.stop_stream()
        stream.close()

        p.terminate()
l = []
for i in range(60):
    l.append(randint(5,10))
m = [7,4,7,4,7,4,7,4,7,4,7,4,7,4,7,4,7,4,7,4,7,4,7,4,7,4,7,4,7,4,7,4,7,4,7,4,7]

kathi = pyAudio(l)
