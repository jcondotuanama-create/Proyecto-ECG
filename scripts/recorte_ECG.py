import matplotlib.pyplot as plt
import wfdb as wf
import pandas as pd
###Path to the ECG DATA. 
Data_path = 'C:/Users/jm635/Documents/Proyecto_ECG/data/15814'
#####Read the ECG data using wfdb
record = wf.rdrecord(Data_path)

###Extract the signal and the sampling frequency
signals = record.p_signal
sampling_frequency = record.fs

####Grafic the first derivation of the ECG signal.
samples_to_plot = sampling_frequency * 5
segment = signals[:samples_to_plot]
plt.figure(figsize=(12, 8))                     # Crea una figura grande
for i in range(signals.shape[1]):               # Itera por cada derivación
    plt.subplot(signals.shape[1], 1, i+1)      # Divide la figura en subplots
    plt.plot(segment[:, i])                    # Grafica la derivación i
    plt.title(f'Derivación {i}')               # Pone título a cada subplot
plt.tight_layout()                              # Ajusta los espacios entre gráficos                                      # Muestra la figura
plt.xlabel("Time (samples)")
plt.ylabel("Amplitude (mV)")
print("Sampling frequency:", sampling_frequency)
print("Signal shape:", signals.shape)
print("Duration of ECG (seconds):", signals.shape[0] / sampling_frequency)
plt.show()


