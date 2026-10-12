import argparse
from pathlib import Path


def transcribe_audio(file_path: str | Path, model_name: str = "base") -> str:
    import whisper

    model = whisper.load_model(model_name)
    result = model.transcribe(str(file_path))
    return result["text"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe an audio file with Whisper.")
    parser.add_argument("file", nargs="?", default="mock_audio.wav")
    parser.add_argument("--model", default="base", help="Whisper model name (default: base)")
    args = parser.parse_args()

    transcription = transcribe_audio(args.file, args.model)
    print("Transcription:", transcription)
