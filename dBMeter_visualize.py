import numpy as np
import matplotlib.pyplot as plt


DELIMITER = ','
FILE_PATH = 'wall.txt' #example file

# plik z danymi
with open(FILE_PATH) as csvFile:
  n_cols = len(csvFile.readline().split(DELIMITER))

  # moc sygnału w danym zakresie częstliwości dla każdej sekundy pomiaru
  freqData = np.loadtxt(FILE_PATH, delimiter=DELIMITER, skiprows=1, usecols=np.arange(2, n_cols))
  # poziom głoności w całym paśmie dla każdej sekundy pomiaru
  loudnessData = np.loadtxt(FILE_PATH, delimiter=DELIMITER, skiprows=1, usecols=2)
  # etykiety danych do wizualiacji
  labels = np.loadtxt(FILE_PATH, dtype=str, delimiter=DELIMITER, max_rows=1, usecols=np.arange(2,n_cols))

  # uśrednienie mocy sygnału w poszczególnych pasmach za cały okres pomiaru
  meanFreqData = np.mean(freqData,axis=0)

  '''
  Przykładowe zobrazowanie widma i zmierzonych poziomów głośności dla średniej
  ze wszystkich pomiarów w czasie.
  '''

  plt.figure(figsize=(8, 10),dpi=200)
  plt.plot(range(2, n_cols), meanFreqData)
  plt.bar(range(2, n_cols), meanFreqData)
  plt.xticks(range(2, n_cols), labels, rotation=90, fontsize=9)
  plt.yticks(fontsize=9)
  plt.xlabel('t[s]')
  plt.ylabel('dB')
  plt.title('Uśrednione widmo w calym paśmie')
  plt.show()


  plt.figure(figsize=(8, 10),dpi=200)
  plt.plot(loudnessData)
  plt.title('Poziom głośności w całym paśmie')
  plt.xlabel('t[s]')
  plt.ylabel('dB')
  plt.show()
