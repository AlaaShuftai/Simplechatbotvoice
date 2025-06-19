# 🎙️ Smart Voice Assistant — Runs Locally, Responds Like a Human

Welcome! This is a simple yet powerful voice assistant project that runs 100% locally on your machine — no paid APIs, no internet required, and no OpenAI key. http://127.0.0.1:7860

Just speak into your mic, and it will listen, understand, respond, and speak back to you 🔁🧠🔊


---

## 🧠 How It Works

1. You speak through the Gradio interface
   ![gradio-logo-png_seeklogo-515011](https://github.com/user-attachments/assets/c122637a-eff6-4992-9061-69ad651266c1)
2. Your voice is transcribed into text using [Whisper](https://github.com/openai/whisper)                                                                                       ![ollama-logo-png_seeklogo-593420](https://github.com/user-attachments/assets/ef336bb4-cd04-48d0-9ff3-68c75de3677f)
3. The transcribed text is passed to [LLaMA 3](https://ollama.com) running locally via [Ollama](https://ollama.com)
4. A smart response is generated using `LangChain`                                                                                                                              ![langchain-logo-png_seeklogo-611654](https://github.com/user-attachments/assets/cc5f6370-7213-4965-a143-655df54b9630)
5. The response is converted into audio using `gTTS` and played back in the browser

![google-text-to-speech-logo-png_seeklogo-332738](https://github.com/user-attachments/assets/a34e3599-38bf-4b24-ac7b-272b8f29fae2)

---

## 🛠️ Technologies Used

| Library | Purpose |
|--------|---------|
| [`gradio`](https://www.gradio.app/) | For the user-friendly voice interface |
| [`whisper`](https://github.com/openai/whisper) | Transcribes spoken audio to text |
| [`ollama`](https://ollama.com) + `LLaMA 3` | Runs the language model locally |
| [`langchain`](https://python.langchain.com/) | To work with LLaMA in Python |
| [`gTTS`](https://pypi.org/project/gTTS/) | Converts AI response to speech (mp3) |

---

## 🚀 How to Run the Project

```bash
# 1. Activate your virtual environment
conda activate voicechatbot

# 2. Start the LLaMA 3 model in the background
ollama run llama3

# 3. Launch the assistant
python assistant_gradio.py
