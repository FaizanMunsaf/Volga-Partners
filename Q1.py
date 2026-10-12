from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile

app = FastAPI()

SUPPORTED_FORMATS = {".wav", ".mp3"}


@app.post("/audio")
async def accept_audio(file: UploadFile = File(...)) -> dict[str, str | int]:
    filename = file.filename or ""
    file_extension = Path(filename).suffix.lower()

    if file_extension not in SUPPORTED_FORMATS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported audio format. Use one of: {', '.join(sorted(SUPPORTED_FORMATS))}",
        )

    if not await file.read(1):
        raise HTTPException(status_code=400, detail="Uploaded audio file is empty")

    return {
        "filename": filename,
        "content_type": file.content_type or "application/octet-stream",
        "status": "Accepted successfully",
    }
