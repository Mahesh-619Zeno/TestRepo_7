import librosa
import librosa.display
import matplotlib.pyplot
import numpy
import os

# Load a sample audio file
file_path = 'sample.wav'

if os.path.exists(file_path):
    # Load the audio
    audio_data, sample_rate = librosa.load(file_path)

    # Calculate a short-time Fourier transform (STFT)
    stft = numpy.abs(librosa.stft(audio_data))

    # Convert amplitude to decibels
    db_spectrogram = librosa.amplitude_to_db(stft, ref=numpy.max)

    # Plot the spectrogram
    matplotlib.pyplot.figure(figsize=(8, 3))
    librosa.display.specshow(db_spectrogram, sr=sample_rate, x_axis='time', y_axis='log')
    matplotlib.pyplot.title('Spectrogram (dB)')
    matplotlib.pyplot.colorbar(format='%+2.0f dB')
    matplotlib.pyplot.tight_layout()

    # Save the plot
    output_path = 'output_plot.png'
    matplotlib.pyplot.savefig(output_path)
    print(f"Spectrogram saved to {output_path}")

else:
    print(f"File not found: {file_path}")
