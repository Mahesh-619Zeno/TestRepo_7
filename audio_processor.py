import os
import librosa
import librosa.display
import matplotlib.pyplot
import numpy

# Setup
audio_file = 'sample.wav'
file_path = os.path.join('.', audio_file)

# Load audio if it exists
if os.path.exists(file_path):
    y, sr = librosa.load(file_path)
    duration = librosa.get_duration(y=y, sr=sr)
    print("Duration:", duration)

    mean_amplitude = numpy.mean(numpy.abs(y))
    print("Mean amplitude:", round(mean_amplitude, 4))

    # Create spectrogram
    spec = numpy.abs(librosa.stft(y))
    db_spec = librosa.amplitude_to_db(spec)

    # Plot
    matplotlib.pyplot.figure()
    librosa.display.specshow(db_spec, sr=sr, x_axis='time', y_axis='log')
    matplotlib.pyplot.title("Spectrogram")
    matplotlib.pyplot.colorbar()
    matplotlib.pyplot.show()
else:
    print("Audio file not found.")
