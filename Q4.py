import argparse
from pathlib import Path

from pydub import AudioSegment


def convert_to_wav(input_path: str | Path, output_path: str | Path) -> Path:
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.is_file():
        raise FileNotFoundError(f"Audio file not found: {input_path}")

    audio = AudioSegment.from_file(str(input_path))
    audio.export(str(output_path), format="wav")
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an audio file to WAV.")
    parser.add_argument("input", nargs="?", default="mock_audio.wav")
    parser.add_argument("output", nargs="?", default="converted_audio.wav")
    args = parser.parse_args()

    wav_path = convert_to_wav(args.input, args.output)
    print(f"Converted audio saved to: {wav_path}")
