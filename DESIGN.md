
## Design decisions

- **Q1: Upload API:** FastAPI accepts WAV and MP3 uploads and rejects
  unsupported extensions or empty files with an HTTP 400 response. The API
  validates the upload; it does not save the uploaded file.
- **Q2 and Q3: Transcription:** Both use OpenAI Whisper. The `tiny` model is
  used in the demo commands because it downloads and runs faster; use another
  Whisper model (such as `base`) when you prefer a potentially more accurate
  transcription over speed. Q2 returns the full text, while Q3 reports the
  start and end times Whisper provides for each segment.
- **Q4: Format conversion:** Pydub converts the input to WAV, a common format
  accepted by speech models. Pydub uses FFmpeg to decode and encode many audio
  formats, so FFmpeg must be installed and on `PATH`.
- **Q5: Long audio:** The default `chunk_seconds=600` means ten-minute chunks.
  This is a practical starting point that keeps each piece smaller than
  processing an entire long recording at once, while avoiding a very large
  number of tiny files. Choose a shorter duration if memory or processing
  limits require it, or a longer duration if your model/service supports it.
  The demo overrides the default with 8 seconds only to show chunking on the
  short mock sample. Q5 creates WAV chunks; it does not itself transcribe or
  combine them.
- **Local sample and runtime:** The mock speech is generated locally by
  Windows' built-in speech synthesizer. The Windows dependency setup uses
  CPU-only Torch so Whisper does not require a CUDA-capable GPU.
