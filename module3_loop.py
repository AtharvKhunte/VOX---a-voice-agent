import speech_recognition as sr
import subprocess

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

        if user_text.strip().lower() in ("exit", "goodbye"):
            speak("Goodbye!")
            break

        speak(f"You said: {user_text}")

if __name__ == "__main__":
    main()