import scipy.io.wavfile as wavfile
import numpy as np
import pylab as pl
rate, data = wavfile.read('piano2.wav')
print(rate, end="\n")
#t = np.arange(len(data[:,0]))*1.0/rate
#pl.plot(t, data[:,0])
#pl.show()



#another way to plot the values are.

p = 20*np.log10(np.abs(np.fft.rfft(data[:2048, 0])))
f = np.linspace(0, rate/2.0, len(p))
pl.plot(f, p)
pl.xlabel("Frequency(Hz)")
pl.ylabel("Power(dB)")
pl.show()
