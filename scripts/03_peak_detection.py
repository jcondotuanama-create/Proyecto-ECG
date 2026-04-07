import wfdb as wf
import numpy as np
import matplotlib
# --- FORCE GRAPHIC MOTOR ---
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
# ----------------------------

# 1. Data loading
data_path = 'C:/Users/jm635/Documents/Proyecto_ECG/data/15814'
record = wf.rdrecord(data_path)
fs = record.fs
signal = record.p_signal[:fs*10, 0] 

# 2. Vectorized Peak Detection
time = np.arange(len(signal)) / fs # Create a time vector based on the length of the signal and the sampling frequency

# --- DETECTION OF PEAKS ---
signal_inverted = -signal 
threshold = np.mean(signal_inverted) + 2 * np.std(signal_inverted)
over_threshold = np.where(signal_inverted > threshold)[0]

peaks = []
if len(over_threshold) > 0:
    peaks.append(over_threshold[0])
    for i in range(1, len(over_threshold)):
        if over_threshold[i] - over_threshold[i-1] > (fs * 0.5):
            peaks.append(over_threshold[i])
peaks = np.array(peaks)

# 4. BPM
bpm = (len(peaks) / (len(signal)/fs)) * 60
print(f"Detected Heart Rate: {bpm:.2f} BPM")

# 5. Visualization

plt.figure(figsize=(12, 4))
plt.plot(time, signal, label='ECG Signal (Derivación 0)', color='black', lw=1)
plt.plot(time[peaks], signal[peaks], "x", color='red', label='Maximums R detected')
plt.title(f'ECG analisis - Frequency: {bpm:.2f} BPM')
plt.xlabel('Time (Seconds)')
plt.ylabel('Voltage (mV)')
plt.legend()
plt.grid(alpha=0.3)
# 6. Save the graphic
import os
if not os.path.exists('results'): os.makedirs('results') # Create results folder if it does not exist

plt.savefig('results/analisis_66_bpm.png', dpi=300) # Save the graphic with a name that includes the detected BPM for easy identification. Adjust the name as needed for different records or BPM values.
print(" Análisis completed. Graphic saved in: results/analisis_66_bpm.png")
plt.close() # Close the plot to free up memory, especially if we are processing multiple records in a loop. 

