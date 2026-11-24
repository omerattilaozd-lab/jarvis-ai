
from pathlib import Path
from faster_whisper import WhisperModel

# Daha önce kaydettiğimiz mikrofon sesi
AUDIO_FILE = Path("/tmp/jarvis-mic-test3.wav")

def main():
    if not AUDIO_FILE.exists():
        print("HATA: Ses kaydı bulunamadı.")
        return

    print("JARVIS: Ses tanıma modeli yükleniyor...")

    # İlk test CPU üzerinde yapılacak
    model = WhisperModel(
        "base",
        device="cpu",
        compute_type="int8"
    )

    print("JARVIS: Ses kaydı analiz ediliyor...")

    segments, info = model.transcribe(
    str(AUDIO_FILE),
    beam_size=5,
    vad_filter=True,
    language="tr"

    )

    text = " ".join(
        segment.text.strip() for segment in segments
    ).strip()

    print(f"Algılanan dil: {info.language}")
    print(f"Algılanan konuşma: {text or '(Konuşma algılanamadı)'}")


if __name__ == "__main__":
    main()
