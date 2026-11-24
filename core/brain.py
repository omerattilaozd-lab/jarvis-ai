
import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "gemma3:latest"

SYSTEM_PROMPT = """
Sen J.A.R.V.I.S. adında kişisel bir yapay zekâ asistanısın.
Daima Türkçe konuş.
Sakin, zeki, profesyonel ve yardımsever ol.
Kullanıcıya efendim diye hitap edebilirsin.
Cevaplarını doğal, anlaşılır ve genellikle kısa tut.
Kendini Google'ın modeli olarak tanıtma.
Bilmediğin konularda dürüst ol.
"""

def ask_jarvis(question):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        "stream": False
    }

    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(request, timeout=120) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["message"]["content"]


if __name__ == "__main__":
    print("J.A.R.V.I.S. beyni aktif!")

    while True:
        question = input("\nSen: ").strip()

        if question.lower() in ["çık", "exit", "quit"]:
            break

        if not question:
            continue

        try:
            answer = ask_jarvis(question)
            print(f"\nJARVIS: {answer}")
        except Exception as error:
            print(f"Hata: {error}")
