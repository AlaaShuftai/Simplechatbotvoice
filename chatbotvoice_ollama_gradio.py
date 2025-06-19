import gradio as gr
import whisper, uuid, os
from langchain_ollama.chat_models import ChatOllama
from langchain.schema import HumanMessage
from gtts import gTTS

# Whisper تحويل الصوت إلى نص
model_whisper = whisper.load_model("base")

def audio_to_text(file_path):
    result = model_whisper.transcribe(file_path)
    return result["text"]

# LLaMA 3 توليد الرد
model_llama = ChatOllama(model="llama3")

def generate_response(prompt):
    reply = model_llama.invoke([HumanMessage(content=prompt)])
    return reply.content

# تحويل النص إلى صوت
def text_to_speech(text):
    fname = f"{uuid.uuid4()}.mp3"
    gTTS(text=text, lang="en").save(fname)
    return fname

# دالة Gradio الشاملة
def voice_assistant(audio_file):
    user_text = audio_to_text(audio_file)
    assistant_reply = generate_response(user_text)
    reply_audio = text_to_speech(assistant_reply)
    return user_text, assistant_reply, reply_audio

demo = gr.Interface(
    fn=voice_assistant,
    inputs=gr.Audio(sources=["microphone"], type="filepath", label="سجّل صوتك"),
    outputs=[
        gr.Textbox(label="ما قاله المستخدم"),
        gr.Textbox(label="رد المساعد"),
        gr.Audio(label="الرد الصوتي"),
    ],
    title="Ano's chatbotvoice"
)

if __name__ == "__main__":
    demo.launch()