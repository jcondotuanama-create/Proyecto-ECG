import wfdb as wf
import numpy as np

data_path = 'C:/Users/jm635/Documents/Proyecto_ECG/data/15814'

record = wf.rdrecord(data_path)

signals = record.p_signal
fs = record.fs

signal = signals[:fs*5, 0]

threshold = np.mean(signal) + 1.5*np.std(signal)

peaks = np.where(signal > threshold)[0]

print("Detected peaks:", peaks)
print("Total number of peaks:", len(peaks))