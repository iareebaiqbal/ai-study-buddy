import gradio as gr
from groq import Groq
import os

client = Groq(api_key=os.getenv("API_Key"))

def get_response(message, history):
    messages = [
        {"role": "system", "content": "You are a helpful study assistant. Answer any question on any topic clearly and in detail."}
    ]
    
    for item in history:
        messages.append({"role": "user", "content": item["content"] if isinstance(item, dict) else item[0]})
        
    messages.append({"role": "user", "content": message})
    
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages,
            max_tokens=1024,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("# 📚 AI Study Buddy\n### Your smart learning assistant 🚀")
    gr.ChatInterface(
        fn=get_response,
        description="Ask me anything about any subject!",
        type="messages"
    )

demo.launch(theme=gr.themes.Soft())
