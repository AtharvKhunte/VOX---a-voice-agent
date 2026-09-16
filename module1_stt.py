import speech_recognition as sr

def listen_loop():
    r = sr.Recognizer()
    mic = sr.Microphone()

    # calibrate for ambient noise once
    with mic as source:
        print("Adjusting for background noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Ready. Speak now (say 'exit' to quit).")

    while True:
        with mic as source:
            try:
                audio = r.listen(source)
            except KeyboardInterrupt:
                print("Stopped.")
                break

        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")

            if text.strip().lower() == "exit":
                print("Exiting.")
                break

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"API error: {e}")

if __name__ == "__main__":
    listen_loop()