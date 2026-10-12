import argparse
from pathlib import Path

from pydub import AudioSegment


def split_audio(
    input_path: str | Path,
    output_dir: str | Path,
    chunk_seconds: int = 600,
) -> list[Path]:
    input_path = Path(input_path)
    output_dir = Path(output_dir)

    if not input_path.is_file():
        raise FileNotFoundError(f"Audio file not found: {input_path}")
    if chunk_seconds <= 0:
        raise ValueError("chunk_seconds must be greater than zero")

    output_dir.mkdir(parents=True, exist_ok=True)
    audio_format = input_path.suffix.lstrip(".") or None
    chunks = []
    start_seconds = 0
    chunk_index = 0

    while True:
        chunk = AudioSegment.from_file(
            str(input_path),
            format=audio_format,
            start_second=start_seconds,
            duration=chunk_seconds,
        )
        if len(chunk) == 0:
            break

        chunk_path = output_dir / f"chunk_{chunk_index:03d}.wav"
        chunk.export(str(chunk_path), format="wav")
        chunks.append(chunk_path)

        start_seconds += chunk_seconds
        chunk_index += 1

    return chunks


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split audio into WAV chunks.")
    parser.add_argument("input", nargs="?", default="mock_audio.wav")
    parser.add_argument("output_dir", nargs="?", default="audio_chunks")
    parser.add_argument(
        "--chunk-seconds",
        type=int,
        default=600,
        help="Maximum duration of each chunk in seconds (default: 600)",
    )
    args = parser.parse_args()

    chunks = split_audio(args.input, args.output_dir, chunk_seconds=args.chunk_seconds)
    print(f"Created {len(chunks)} chunks:")
    for chunk in chunks:
        print(chunk)
