from tkinter import *
import pyaudio
import numpy as np

f = 440
class Kathi(object):
    def __init__(self, root):
        self.w = Scale(root, from_=0, to=10, command=self.print_value)
        self.w.pack(fill=BOTH)
    def print_value(self,val):
        print(val, end="\n")
        generateAudio(440-int(val)*40)
        
root = Tk()
root.geometry("400x300")
kathi = Kathi(root)

def generateAudio(f):
    
    p = pyaudio.PyAudio()

    volume = 0.5     # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 10.0   # in seconds, may be float
        #f = 440.0        # sine frequency, Hz, may be float

        # generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

        # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)

        # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*samples)

    stream.stop_stream()
    stream.close()

    p.terminate()

    
root.mainloop()

