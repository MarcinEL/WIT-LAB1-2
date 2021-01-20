import numpy as np
import matplotlib.pyplot as plt

# plik z danymi 
with open("/content/drive/MyDrive/dbmeter.txt") as f:
  n_cols = len(f.readline().split("\t"))

# moc sygnału w danym zakresie częstliwości dla każdej sekundy pomiaru
freqData = np.loadtxt('/content/drive/MyDrive/dbmeter.txt', skiprows=1, usecols=np.arange(3,n_cols+1))
# poziom głoności w całym paśmie dla każdej sekundy pomiaru
loudnessData = np.loadtxt('/content/drive/MyDrive/dbmeter.txt', skiprows=1, usecols=2)
# etykiety danych do wizualiacji
labels = np.loadtxt('/content/drive/MyDrive/dbmeter.txt', dtype=str, max_rows=1, usecols=np.arange(2,n_cols))

# uśrednienie mocy sygnału w poszczególnych pasmach za cały okres pomiaru
meanFreqData = np.mean(freqData,axis=0)

'''
Przykładowe zobrazowanie widma i zmierzonych poziomów głośności dla średniej
ze wszystkich pomiarów w czasie.
'''
plt.figure(figsize=(4,3),dpi=200)
plt.plot(range(1,n_cols-1),meanFreqData)
plt.bar(range(1,n_cols-1),meanFreqData)
plt.xticks(range(1,n_cols-1), labels, rotation=90, fontsize=6)
plt.yticks(fontsize=6)
plt.title('Uśrednione widmo w pasmach oktawowych')

plt.figure(figsize=(4,3),dpi=200)
plt.plot(loudnessData)
plt.title('Poziom głośności')
