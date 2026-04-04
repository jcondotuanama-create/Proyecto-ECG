import wfdb as wf
import numpy as np

data_path = 'C:/Users/jm635/Documents/Proyecto_ECG/data/15814'

record = wf.rdrecord(data_path)

signals = record.p_signal
fs = record.fs

signal = -signals[:fs*5, 0] ##We invert the signal because in this particular record, the peaks are negative. This is just a matter of convention and it does not affect the analysis. We can adjust this if we want to work with the original signal.  


threshold = np.mean(signal) + 2*np.std(signal) #This is the umbral that we will use to detect the peaks. We can adjust it if we want to be more or less strict in our detection.    


peaks = np.where(signal > threshold)[0] #Here we detect the peaks by finding the indices where the signal is greater than the threshold. This will give us a list of indices where the peaks are located. We can then use these indices to extract the corresponding values from the signal if we want to analyze them further. 


# 4. FILTRO OF ENGIINERGIN: We want to keep only the peaks that are at least 0.5 seconds apart (to avoid detecting the same heartbeat multiple times)   
real_peaks = []
if len(peaks) > 0:
    real_peaks.append(peaks[0]) # We always keep the first  detected peak
    for i in range(1, len(peaks)):
        # If the current peak is more than 0.5 seconds away from the last accepted peak, we consider it a real heartbeat    
        if peaks[i] - real_peaks[-1] > (fs * 0.5):
            real_peaks.append(peaks[i])

print(f"Real heartbeats detected: {len(real_peaks)}")
