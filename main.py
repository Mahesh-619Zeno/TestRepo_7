import os
from typing import Tuple, Optional

import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

DEFAULT_AUDIO_FILE = 'sample.wav'

def load_audio(file_path: str) -> Tuple[Optional[np.ndarray], Optional[int]]:
    """Load an audio file using librosa.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        Tuple of audio time series (y) and sampling rate (sr), or (None, None) on failure.
    """
    try:
        y, sr = librosa.load(file_path, sr=None)
        duration = librosa.get_duration(y=y, sr=sr)
        print(f"[load_audio] Loaded '{file_path}' | Duration: {duration:.2f} seconds")
        return y, sr
    except Exception as e:
        print(f"[load_audio] Failed to load audio: {e}")
        return None, None

def plot_spectrogram(y: np.ndarray, sr: int) -> None:
    """Generate and display a spectrogram of the audio signal.

    Args:
        y (np.ndarray): Audio time series.
        sr (int): Sampling rate.
    """
    spec = np.abs(librosa.stft(y))
    db_spec = librosa.amplitude_to_db(spec, ref=np.max)

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(db_spec, sr=sr, x_axis='time', y_axis='log')
    plt.title("Spectrogram")
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    plt.show()

def main(audio_file: str = DEFAULT_AUDIO_FILE) -> None:
    file_path = os.path.abspath(audio_file)

    if not os.path.isfile(file_path):
        print(f"[main] Audio file not found: {file_path}")
        return

    y, sr = load_audio(file_path)
    if y is not None and sr is not None:
        plot_spectrogram(y, sr)

if __name__ == "__main__":
    main()
