import gradio as gr
import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=os.getenv("API_Key")
)

def get_response(message, history):
    messages = [
        {"role": "system", "content": "You are a helpful study assistant. Answer any question on any topic clearly and in detail."}
    ]
    
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})
    
    messages.append({"role": "user", "content": message})
    
    try:
        response = client.chat_completion(
            messages=messages,
            max_tokens=1024,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📚 AI Study Buddy\n### Your smart learning assistant 🚀")
    gr.ChatInterface(
        fn=get_response,
        description="Ask me anything about any subject!",
    )

demo.launch()