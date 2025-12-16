import librosa
import matplotlib.pyplot as plt

import sys
audio = sys.argv[1] # Path provided as a command-line argument

x, sr = librosa.load(audio)
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize = (10, 5))
librosa.display.specshow(Xdb, sr = sr, x_axis = 'time', y_axis = 'hz')
plt.colorbar()
plt.title('Spectrogram of '+ audio)
plt.show()  # This will show the plot