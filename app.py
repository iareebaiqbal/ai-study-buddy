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

def chat(message, history):
    # Convert history to messages format
    messages = [
        {
            "role": "system",
            "content": """You are an expert study assistant. You can answer questions on ANY topic:
- Computer Science (Python, Networks, OOP, OS, Database, AI/ML)
- Mathematics, Physics, Chemistry, Biology
- History, Geography, Literature
- Any other subject or general knowledge

Give clear, detailed, and educational answers. Always be helpful."""
        }
    ]
    
    for user_msg, bot_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": bot_msg})
    
    messages.append({"role": "user", "content": message})
    
    response = client.chat_completion(
        messages=messages,
        max_tokens=1024,
        temperature=0.7,
    )
    
    return response.choices[0].message.content

# =========================
# 🎨 GRADIO UI
# =========================

with gr.Blocks(
    theme=gr.themes.Soft(primary_hue="violet"),
    title="AI Study Buddy"
) as demo:
    
    gr.Markdown("""
    # 📚 AI Study Buddy
    ### Your smart learning assistant 🚀
    Ask me anything about **any subject** — no restrictions!
    """)
    
    chatbot = gr.Chatbot(
        label="Study Assistant",
        height=450,
        show_copy_button=True,
        avatar_images=("👤", "🤖")
    )
    
    with gr.Row():
        msg = gr.Textbox(
            placeholder="Koi bhi question poochein...",
            label="",
            scale=9,
            autofocus=True
        )
        send = gr.Button("➤", scale=1, variant="primary")
    
    with gr.Row():
        gr.Examples(
            examples=[
                "Tell me about Python",
                "What is OOP?",
                "Explain Neural Networks",
                "What is photosynthesis?",
                "Solve: 2x + 5 = 15"
            ],
            inputs=msg
        )
    
    clear = gr.ClearButton([msg, chatbot], value="🗑️ Clear Chat")
    
    def respond(message, history):
        if not message.strip():
            return "", history
        bot_reply = chat(message, history)
        history.append((message, bot_reply))
        return "", history
    
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    send.click(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
  