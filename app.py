import gradio as gr
import os
from huggingface_hub import InferenceClient

# =========================
# 🔥 BACKEND FUNCTION
# =========================

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    token=os.getenv("API_Key")
)

def get_response(message, history):
    messages = [
        {"role": "system", "content": """You are an expert AI Study Buddy 📚. 
Help students with ANY subject — Computer Science, Math, Physics, Chemistry, Biology, History, English, or anything else.
Give clear, simple, and detailed explanations.
Use examples where possible. Be friendly and encouraging! 🌟"""}
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


# =========================
# 🎨 FRONTEND UI
# =========================

custom_css = """
body {
    background: #0f172a;
    font-family: Arial;
}
.gradio-container {
    max-width: 900px !important;
    margin: auto !important;
}
.message.user {
    background-color: #2563eb !important;
    color: white !important;
    border-radius: 15px !important;
}
.message.bot {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 15px !important;
}
textarea {
    border-radius: 10px !important;
}
"""

# =========================
# 🚀 APP LAUNCH
# =========================

with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    # 📚 AI Study Buddy
    ### Your smart learning assistant 🚀
    """)

    gr.ChatInterface(
        fn=get_response,
        title="Study Assistant",
        description="Ask me anything about any subject!",
        examples=[
            "Tell me about Python",
            "What is OOP?",
            "Explain photosynthesis",
            "What is Pythagoras theorem?",
            "Tell me about World War 2"
        ]
    )

demo.launch()