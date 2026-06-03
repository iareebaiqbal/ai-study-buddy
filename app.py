import gradio as gr
import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    model="meta-llama/Llama-3.1-8B-Instruct",
    token=os.getenv("API_Key")
)

def get_response(message, history):
    messages = [
        {"role": "system", "content": "You are a helpful study assistant. Answer any question on any topic clearly and in detail."}
    ]
    
    for item in history:
        if isinstance(item, dict):
            messages.append({"role": item["role"], "content": item["content"]})
        else:
            messages.append({"role": "user", "content": item[0]})
            messages.append({"role": "assistant", "content": item[1]})
    
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

with gr.Blocks() as demo:
    gr.Markdown("# 📚 AI Study Buddy\n### Your smart learning assistant 🚀")
    gr.ChatInterface(
        fn=get_response,
        description="Ask me anything about any subject!",
    )

demo.launch(theme=gr.themes.Soft())