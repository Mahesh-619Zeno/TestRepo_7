import os
from pathlib import Path
from typing import Tuple, Optional

import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt


AUDIO_FILE = "sample.wav"


def load_audio(file_path: Path) -> Tuple[Optional[np.ndarray], Optional[int]]:
    """Load an audio file using librosa.

    Args:
        file_path (Path): Path to the audio file.

    Returns:
        Tuple containing the audio time series (y) and sample rate (sr),
        or (None, None) if loading fails.
    """
    try:
        y, sr = librosa.load(str(file_path))
        duration = librosa.get_duration(y=y, sr=sr)
        print(f"Loaded '{file_path.name}' | Duration: {duration:.2f}s")
        return y, sr
    except Exception as exc:
        print(f"Error loading audio '{file_path}': {exc}")
        return None, None


def plot_spectrogram(y: np.ndarray, sr: int) -> None:
    """Generate and display a spectrogram of the audio signal."""
    spec = np.abs(librosa.stft(y))
    db_spec = librosa.amplitude_to_db(spec, ref=np.max)

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(
        db_spec,
        sr=sr,
        x_axis="time",
        y_axis="log"
    )
    plt.title("Spectrogram")
    plt.colorbar(format="%+2.0f dB")
    plt.tight_layout()
    plt.show()


def main(audio_path: str = AUDIO_FILE) -> None:
    """Main application entry point."""
    file_path = Path(audio_path).resolve()

    if not file_path.exists():
        print(f"Audio file not found: {file_path}")
        return

    y, sr = load_audio(file_path)
    if y is not None and sr is not None:
        plot_spectrogram(y, sr)


if __name__ == "__main__":
    main()
