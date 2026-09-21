import speech_recognition as sr
import subprocess
import requests

def speak(text: str):
    print(f"[Agent]: {text}")
    subprocess.run([
        "python", "-c",
        f"import pyttsx3; e=pyttsx3.init(); e.setProperty('rate',170); e.say('''{text}'''); e.runAndWait()"
    ])

# --- STT setup ---
r = sr.Recognizer()
mic = sr.Microphone()

def listen():
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"API error: {e}")
        return None

# --- LLM setup ---
messages = [
    {"role": "system", "content": "You are a concise voice assistant. Limit all responses to 1-2 short sentences maximum."}
]

def ask_ollama(user_text: str) -> str:
    messages.append({"role": "user", "content": user_text})
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={"model": "llama3.2", "messages": messages, "stream": False},
            timeout=30
        )
        response.raise_for_status()
        reply = response.json()["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        return reply
    except requests.exceptions.Timeout:
        return "Sorry, that took too long. Please try again."
    except requests.exceptions.ConnectionError:
        return "I can't reach the local AI server right now."
    except requests.exceptions.RequestException as e:
        print(f"Ollama request failed: {e}")
        return "Something went wrong talking to the AI."
    except (KeyError, ValueError) as e:
        print(f"Unexpected response format: {e}")
        return "I got a strange response, please try again."

# --- Main loop ---
def main():
    speak("Voice pipeline initialized!")

    while True:
        print("Listening...")
        user_text = listen()

        if user_text is None:
            print("Could not understand audio.")
            continue

        print(f"You said: {user_text}")

        if user_text.strip().lower() in ("exit", "bye"):
            speak("Goodbye!")
            break

        reply = ask_ollama(user_text)
        speak(reply)

if __name__ == "__main__":
    main()