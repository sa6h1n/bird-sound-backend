import librosa
import soundfile as sf

def convert_to_wav(input_path: str) -> str:
    y, sr = librosa.load(input_path, sr=48000, mono=True)
    wav_path = input_path.rsplit(".", 1)[0] + ".wav"
    sf.write(wav_path, y, sr)
    return wav_path