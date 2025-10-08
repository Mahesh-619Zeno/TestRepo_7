import librosa
import librosa.display
import matplotlib.pyplot
import numpy
import os

# Extended audio analysis
def analyze_audio_file(file_path):
    try:
        audio_data, sample_rate = librosa.load(file_path)
        print("Loaded audio with", len(audio_data), "samples at", sample_rate, "Hz")

        # Generate spectrogram
        stft_data = numpy.abs(librosa.stft(audio_data))
        db_spectrogram = librosa.amplitude_to_db(stft_data, ref=numpy.max)

        # Plot and save the spectrogram
        matplotlib.pyplot.figure(figsize=(10, 4))
        librosa.display.specshow(db_spectrogram, sr=sample_rate, x_axis='time', y_axis='log')
        matplotlib.pyplot.colorbar(format='%+2.0f dB')
        matplotlib.pyplot.title('Spectrogram')
        matplotlib.pyplot.tight_layout()
        matplotlib.pyplot.savefig("spectrogram_output.png")
        print("Spectrogram saved.")

    except Exception as e:
        print("Error during analysis:", e)

if __name__ == "__main__":
    file_to_process = "sample.wav"
    if os.path.exists(file_to_process):
        analyze_audio_file(file_to_process)
    else:
        print("File not found:", file_to_process)
