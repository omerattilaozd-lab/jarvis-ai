
import subprocess
from pathlib import Path
from TTS.api import TTS


class JarvisSpeaker:
    def __init__(self):
        print("JARVIS: Ses motoru yükleniyor...")

        self.tts = TTS(
            model_name="tts_models/multilingual/multi-dataset/xtts_v2"
        ).to("cuda")

        self.speaker = "Dionisio Schuyler"
        self.output_path = Path("voice_samples/response.wav")
        self.output_path.parent.mkdir(
            parents=True, exist_ok=True
        )

    def speak(self, text):
        print(f"JARVIS konuşuyor: {text}")

        self.tts.tts_to_file(
            text=text,
            speaker=self.speaker,
            language="tr",
            file_path=str(self.output_path)
        )

        subprocess.run(
            ["paplay", str(self.output_path)],
            check=True
        )


if __name__ == "__main__":
    speaker = JarvisSpeaker()
    speaker.speak(
       
    "Efendim, Jarvis sistemleri aktif. Size nasıl yardımcı olabilirim?"
)
