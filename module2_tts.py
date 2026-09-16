import pyttsx3

# init engine once
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # ~170 WPM, natural pace

def speak(text: str):
    print(f"[Agent]: {text}")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello, I am your assistant.")
    speak("Offline text to speech is now working.")
    speak("Exiting the test block now.")