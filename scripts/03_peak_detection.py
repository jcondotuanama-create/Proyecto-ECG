import wfdb as wf
import numpy as np
import matplotlib
# --- FORZAR MOTOR GRÁFICO ---
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
# ----------------------------

# 1. Carga de datos
data_path = 'C:/Users/jm635/Documents/Proyecto_ECG/data/15814'
record = wf.rdrecord(data_path)
fs = record.fs
signal = record.p_signal[:fs*10, 0] 

# 2. Vector de tiempo
time = np.arange(len(signal)) / fs

# --- DETECCIÓN CORREGIDA ---
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

# 5. Visualización con SEGURO DE CIERRE

plt.figure(figsize=(12, 4))
plt.plot(time, signal, label='ECG Signal (Derivación 0)', color='black', lw=1)
plt.plot(time[peaks], signal[peaks], "x", color='red', label='Maximums R detected')
plt.title(f'ECG analisis - Frequency: {bpm:.2f} BPM')
plt.xlabel('Time (Seconds)')
plt.ylabel('Voltage (mV)')
plt.legend()
plt.grid(alpha=0.3)
# EN LUGAR DE plt.show(), GUARDAMOS EL ARCHIVO
import os
if not os.path.exists('results'): os.makedirs('results') # Crea carpeta si no existe

plt.savefig('results/analisis_66_bpm.png', dpi=300) # Guarda en alta calidad
print("✅ Análisis completado. Gráfica guardada en: results/analisis_66_bpm.png")
plt.close() # Cierra la memoria limpiamente    

