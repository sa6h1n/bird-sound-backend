import os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from bird_ai import analyze_bird_audio
from audio_utils import convert_to_wav

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/analyze")
async def analyze_audio(file: UploadFile = File(...)):
    input_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(input_path, "wb") as f:
        f.write(await file.read())

    wav_path = convert_to_wav(input_path)
    predictions = analyze_bird_audio(wav_path)

    return {
        "predictions": predictions,
        "status": "Analysis complete"
    }