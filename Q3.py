import argparse
from pathlib import Path


def transcribe_with_timestamps(
    file_path: str | Path,
    model_name: str = "base",
) -> list[dict[str, float | str]]:
    import whisper

    model = whisper.load_model(model_name)
    result = model.transcribe(str(file_path))

    return [
        {
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"].strip(),
        }
        for segment in result.get("segments", [])
    ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Transcribe audio and print Whisper's segment timestamps."
    )
    parser.add_argument("file", nargs="?", default="mock_audio.wav")
    parser.add_argument("--model", default="base", help="Whisper model name (default: base)")
    args = parser.parse_args()

    segments = transcribe_with_timestamps(args.file, args.model)
    for segment in segments:
        print(
            f"[{segment['start']:.2f}s - {segment['end']:.2f}s]: "
            f"{segment['text']}"
        )
