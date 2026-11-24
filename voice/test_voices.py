
from pathlib import Path
from TTS.api import TTS

print("JARVIS: Ses modeli yükleniyor...")

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2"
).to("cuda")

speaker = "Dionisio Schuyler"
text = "Dinliyorum efendim."

output_dir = Path("voice_samples")
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "jarvis.wav"

print("JARVIS: Ses oluşturuluyor...")

tts.tts_to_file(
    text=text,
    speaker=speaker,
    language="tr",
    file_path=str(output_file)
)

print(f"JARVIS: Ses hazır! {output_file}")
