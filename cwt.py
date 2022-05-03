#Import the necessary python libraries
import numpy as np
import matplotlib.pyplot as plt
import pywt
import pandas as pd
import pyxdf

#Load the .xdf file into python
data, header = pyxdf.load_xdf('firstname.xdf')

for stream in data:
    y = stream['time_series']
if isinstance(y, list):
        # list of strings, draw one vertical line for each marker
        for timestamp, marker in zip(stream['time_stamps'], y):
            #plt.axvline(x=timestamp)
            print(f'Marker "{marker[0]}" @ {timestamp:.2f}s')
    elif isinstance(y, np.ndarray):
            # numeric data, draw as lines
            plt.plot(stream['time_stamps'], y)
    else:
        raise RuntimeError('Unknown stream format')
plt.show()

#select a signal from the 8 electrode signals
signal1 = data[0] 
#select a range corresponding to an event
g1 = signal1[range_1:range_2]
scales=np.arange(1,400)
#Perform Continuous Wavelet Transform and plot the output
cooef2,freqs = pywt.cwt(g2, scales, 'morl')
plt.figure(figsize=(10,10))
plt.matshow(cooef2)
plt.show()

#select a signal from the 8 electrode signals
signal2 = data[0]
#select a range corresponding to an event
r1 = signal3[range_1:range_2]
scales=np.arange(1,700)
#Perform Continuous Wavelet Transform and plot the output
cooef3,freqs = pywt.cwt(g3, scales, 'morl')
plt.figure(figsize=(10,10))
plt.matshow(cooef3)
plt.show()
