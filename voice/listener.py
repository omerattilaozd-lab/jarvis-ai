
import subprocess
import numpy as np
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
RECORD_SECONDS = 4

print("JARVIS: Ses tanıma sistemi başlatılıyor...")

# Modeli bir kez yükle, sonraki kayıtlarda tekrar kullan.
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def listen():
    """Mikrofondan 4 saniyelik ses alır."""

    command = [
        "timeout", str(RECORD_SECONDS),
        "parec",
        "--raw",
        "--device=@DEFAULT_SOURCE@",
        "--rate=16000",
        "--channels=1",
        "--format=s16le"
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=RECORD_SECONDS + 5
    )

    if result.returncode not in (0, 124):
        error = result.stderr.decode(errors="replace")
        raise RuntimeError(f"Mikrofon hatası: {error}")

    audio = np.frombuffer(
        result.stdout,
        dtype=np.int16
    ).astype(np.float32) / 32768.0

    return audio


def recognize(audio):
    """Kaydedilen konuşmayı yazıya dönüştürür."""

    if len(audio) < SAMPLE_RATE:
        return ""

    segments, info = model.transcribe(
        audio,
        language="tr",
        beam_size=3,
        vad_filter=True,
        condition_on_previous_text=False
    )

    return " ".join(
        segment.text.strip() for segment in segments
    ).strip()


def main():
    print("JARVIS: Mikrofon aktif.")
    print("JARVIS: Beni uyandırmak için 'Jarvis' de.")
    print("Durdurmak için Ctrl+C.\n")

    try:
        while True:
            audio = listen()
            text = recognize(audio)

            if not text:
                continue

            print(f"Duyduğum: {text}")

            normalized = text.casefold()

            if "jarvis" in normalized:
                print("JARVIS: Uyandırma kelimesi algılandı!")
                print("JARVIS: Dinliyorum efendim.\n")

    except KeyboardInterrupt:
        print("\nJARVIS: Dinleme sistemi kapatılıyor.")

    except Exception as error:
        print(f"JARVIS HATA: {error}")


if __name__ == "__main__":
    main()
