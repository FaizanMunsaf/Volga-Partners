# Audio processing demo (Q1–Q5)

## 1. Install the dependencies

From Command Prompt in this folder:

```cmd
venv\Scripts\python.exe -m pip install -r requirements.txt
```

Q2 and Q3 use OpenAI Whisper. Its first run downloads the selected model; use
`--model tiny` for the smallest, fastest demo model. On Windows, the
requirements install a CPU-only Torch build. FFmpeg must also be installed and
available on `PATH` for Pydub to read and export audio.

## 2. Create mock speech audio (optional)

The sample WAV and MP3 are already included in the project folder. To recreate
them on Windows, run the built-in speech synthesizer script from Command
Prompt:

```cmd
powershell -NoProfile -ExecutionPolicy Bypass -File ".\create_mock_audio.ps1"
```

This creates `mock_audio.wav` and `mock_audio.mp3`. You can use your own WAV or
MP3 instead by passing its path to the scripts.

## 3. Run Q1–Q5

From Command Prompt, run Q4 first to convert the mock MP3 to WAV, then run Q2,
Q3, and Q5:

```cmd
venv\Scripts\python.exe Q4.py mock_audio.mp3 converted_audio.wav
venv\Scripts\python.exe Q2.py converted_audio.wav --model tiny
venv\Scripts\python.exe Q3.py converted_audio.wav --model tiny
venv\Scripts\python.exe Q5.py converted_audio.wav audio_chunks --chunk-seconds 8
```

Q2 prints the transcript, Q3 prints transcript segments with timestamps, Q4
converts the MP3 to WAV, and Q5 creates several short WAV chunks. The 8-second
chunk size in this command is deliberately small so the short mock recording
produces multiple chunks for a quick demo.

For Q1, start the upload API in another Command Prompt window:

```cmd
venv\Scripts\python.exe -m uvicorn Q1:app --reload
```

Open <http://127.0.0.1:8000/docs>, expand `POST /audio`, click **Try it out**,
select `mock_audio.mp3`, then click **Execute**. The API accepts `.wav` and
`.mp3` uploads.
