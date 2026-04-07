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

plt.figure(figsize=(12, 8))                     # Create a figure with a specific size
for i in range(signals.shape[1]):               # Iterate over the number of derivations (columns) in the signal
    plt.subplot(signals.shape[1], 1, i+1)      # Divide the figure into subplots for each derivation
    plt.plot(signals[:, i])                    # Plot the signal for the current derivation
    plt.title(f'Derivation {i+1}')               # Set the title for the current subplot
plt.tight_layout()                              # Adjust the spacing between plots
plt.xlabel("Time (samples)")
plt.ylabel("Amplitude (mV)")
print("Sampling frequency:", sampling_frequency)
print("Signal shape:", signals.shape)
print("Duration of ECG (seconds):", signals.shape[0] / sampling_frequency)
plt.show()
#Create a DataFrame with the ECG signals and save it as a CSV file.
df = pd.DataFrame(signals, columns=[f'Derivación {i}' for i in range(signals.shape[1])])
df.to_csv('C:/Users/jm635/Documents/Proyecto_ECG/data/ECG_signals.csv', index=False)

