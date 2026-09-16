<div align="center">

# 🎙️ Voice Agent

### Local Voice-to-LLM Pipeline — Listens. Thinks. Talks back.

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=36BCF7&center=true&vCenter=true&width=500&lines=Listening+for+your+voice...;Talking+to+llama3.2...;Speaking+the+response...;100%25+local.+No+cloud+LLM.)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/LLM-Ollama%20%7C%20llama3.2-black?logo=ollama)
![Status](https://img.shields.io/badge/status-early%20prototype-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)

</div>

---

> 🚧 **Status: Early prototype.** This is the first working version. Expect rapid iteration, breaking changes, and new features soon.

---

## ✨ What it does

- 🎤 **Listens** to your voice via microphone (`SpeechRecognition`)
- 🧠 **Thinks** using a local LLM (`Ollama` + `llama3.2`)
- 🔊 **Speaks back** using offline TTS (`pyttsx3`)
- 🔁 Runs in a continuous conversation loop — say **"exit"** or **"bye"** to stop

All processing happens **on your machine** — speech recognition uses Google's free API for transcription, but the LLM reasoning stays fully local via Ollama.

---

## 🎬 Demo

<div align="center">

<!-- Replace with actual terminal recording GIF -->
`[ demo.gif goes here — record a session with terminalizer / ScreenToGif ] - Comming soon`

</div>

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

<details>
<summary><b>1. Install Python dependencies</b></summary>

```bash
pip install SpeechRecognition pyaudio pyttsx3 requests
```

</details>

<details>
<summary><b>2. Install Ollama & pull the model</b></summary>

```bash
ollama pull llama3.2
ollama serve
```

</details>

<details>
<summary><b>3. System dependencies</b></summary>

**Windows:** Uses built-in SAPI5 — no extra install needed

**Linux:**
```bash
sudo apt install portaudio19-dev espeak
```

</details>

<details>
<summary><b>4. Run it</b></summary>

```bash
python simple_voice_agent.py
```

</details>

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

<details>
<summary><b>🧪 Known Notes / Fixes Applied</b></summary>

- TTS calls run in an isolated subprocess per response — sidesteps a `pyttsx3`/Windows SAPI5 COM bug that silently kills audio on repeated calls in the same process.
- LLM calls use raw `requests` against Ollama's REST API (`/api/chat`) directly, bypassing the official `ollama` Python client due to an unresolved hang issue on some setups.

</details>

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

<div align="center">

## 📄 License

MIT — see [LICENSE](LICENSE)

</div>
