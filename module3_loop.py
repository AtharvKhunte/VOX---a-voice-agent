from voice_utils import speak, listen

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