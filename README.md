# AI Voice Assistant

A modular Python application that turns your microphone and speakers into an AI-powered chatbot. It uses:

- **LangChain + Ollama** (`deepseek-r1`) for conversational AI  
- **SpeechRecognition** (Google Web Speech API) for voice input  
- **gTTS** + **playsound** for text-to-speech output  

You can talk to the bot, and it will speak back its response.

---

## Features

- **Voice Input**: Speak your questions into the mic.  
- **Text Input**: Type your questions in case you prefer.  
- **Voice Output**: Bot replies are spoken aloud.  
- **Modular Structure**: Easy to extend—separate files for model, utilities, and main logic.  
- **Graceful Exit**: Say “exit” or press Ctrl+C to quit.

---

## Prerequisites

- Python 3.8–3.11  
- Ollama running locally with the `deepseek-r1` model downloaded  
- A working microphone and speaker setup  

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/MyTNinja/ai-voice-assistant.git
   cd ai-voice-assistant
