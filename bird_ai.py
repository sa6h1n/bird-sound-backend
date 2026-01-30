from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime

analyzer = Analyzer()

def analyze_bird_audio(audio_path: str):
    recording = Recording(
        analyzer=analyzer,
        path=audio_path,
        date=datetime.now(),
        lat=0.0,
        lon=0.0
    )

    recording.analyze()

    if not recording.detections:
        return []

    valid = [d for d in recording.detections if d["confidence"] >= 0.1]
    valid.sort(key=lambda d: d["confidence"], reverse=True)

    top3 = valid[:3]

    return [
        {
            "bird": d["common_name"],
            "confidence": round(d["confidence"], 2)
        }
        for d in top3
    ]