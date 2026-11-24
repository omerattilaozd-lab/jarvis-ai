
import torch
from TTS.api import TTS

print("JARVIS: XTTS-v2 modeli yükleniyor...")

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2"
).to("cuda")

print("GPU:", torch.cuda.get_device_name(0))
print("Diller:", tts.languages)
print("Hazır sesler:", tts.speakers[:20])
print("JARVIS: Model yükleme başarılı!")
