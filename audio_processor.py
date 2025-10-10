import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Setup
audio_file = 'sample.wav'
file_path = os.path.join('.', audio_file)

# Load audio if it exists
if os.path.exists(file_path):
    try:
        y, sr = librosa.load(file_path, sr=None)
        duration = librosa.get_duration(y=y, sr=sr)
        print(f"Audio loaded successfully: {audio_file}")
        print(f"Sample Rate: {sr}, Duration: {duration:.2f} seconds")

        # Create spectrogram
        spec = np.abs(librosa.stft(y))
        db_spec = librosa.amplitude_to_db(spec, ref=np.max)

        # Plot
        plt.figure(figsize=(10, 4))
        librosa.display.specshow(db_spec, sr=sr, x_axis='time', y_axis='log', cmap='magma')
        plt.title("Spectrogram (dB)")
        plt.colorbar(format='%+2.0f dB')
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error processing audio file:", e)
else:
    print(f"Audio file not found: {file_path}")
