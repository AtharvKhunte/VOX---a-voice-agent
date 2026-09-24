import speech_recognition as sr
import subprocess

# --- TTS ---
def speak(text: str):
    print(f"[Agent]: {text}")
    subprocess.run([
        "python", "-c",
        f"import pyttsx3; e=pyttsx3.init(); e.setProperty('rate',170); e.say('''{text}'''); e.runAndWait()"
    ])

# --- STT ---
r = sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = False
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