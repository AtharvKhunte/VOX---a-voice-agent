# 🎙️ Voice Agent — Local Voice-to-LLM Pipeline

A fully local, privacy-friendly voice assistant that listens, thinks, and talks back — no cloud LLM required.

> 🚧 **Status: Early prototype.** This is the first working version. Expect rapid iteration, breaking changes, and new features soon.

---

## ✨ What it does

- 🎤 **Listens** to your voice via microphone (`SpeechRecognition`)
- 🧠 **Thinks** using a local LLM (`Ollama` + `llama3.2`)
- 🔊 **Speaks back** using offline TTS (`pyttsx3`)
- 🔁 Runs in a continuous conversation loop — say **"exit"** or **"bye"** to stop

All processing happens **on your machine** — speech recognition uses Google's free API for transcription, but the LLM reasoning stays fully local via Ollama.

---

## 🛠️ Tech Stack

| Component | Library |
|---|---|
| Speech-to-Text | `SpeechRecognition` |
| Text-to-Speech | `pyttsx3` |
| LLM Backend | `Ollama` (`llama3.2`) |
| HTTP Client | `requests` |

---

## 📦 Setup

### 1. Install dependencies
```bash
pip install SpeechRecognition pyaudio pyttsx3 requests
```

### 2. Install Ollama & pull the model
```bash
ollama pull llama3.2
ollama serve
```

### 3. System dependencies
- **Windows:** Uses built-in SAPI5 — no extra install needed
- **Linux:**
  ```bash
  sudo apt install portaudio19-dev espeak
  ```

### 4. Run it
```bash
python simple_voice_agent.py
```

---

## 🗣️ Usage

1. Script boots and says: *"Voice pipeline initialized!"*
2. Speak naturally — it transcribes, sends to the LLM, and replies out loud
3. Say **"exit"** or **"bye"** to end the session cleanly

---

## 📁 Project Structure

```
voice_assistant/
├── module1_stt.py         # standalone speech-to-text test
├── module2_tts.py         # standalone text-to-speech test
├── module3_loop.py        # STT + TTS echo loop (no LLM)
├── simple_voice_agent.py  # full pipeline: STT → LLM → TTS
└── logs/
```

---

## 🧪 Known Notes

- TTS calls run in an isolated subprocess per response — sidesteps a `pyttsx3`/Windows SAPI5 COM bug that silently kills audio on repeated calls in the same process.
- LLM calls use raw `requests` against Ollama's REST API (`/api/chat`) directly, bypassing the official `ollama` Python client due to an unresolved hang issue on some setups.

---

## 🗺️ Roadmap

- [ ] Wake-word activation (no manual restart needed)
- [ ] Streaming LLM responses for faster perceived latency
- [ ] Configurable voice/persona
- [ ] Interruptible speech (barge-in support)
- [ ] Local offline STT option (Whisper)
- [ ] Memory persistence across sessions
- [ ] Simple GUI / system tray app

---

## 🤝 Contributing

This is a personal project in active development — issues, ideas, and PRs welcome as it grows.

---

## 📄 License

MIT
