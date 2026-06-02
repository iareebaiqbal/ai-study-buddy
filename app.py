import gradio as gr
from google import genai
import os

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM_PROMPT = """You are a helpful and friendly AI Study Buddy. 
Your job is to help students learn and understand topics clearly.
- Give accurate, detailed explanations
- Use simple language that students can understand
- When making quizzes, provide 4 options (A, B, C, D) with the correct answer at the end
- When making flashcards, format them clearly as Question and Answer pairs
- Always be encouraging and supportive"""

def chat(message, history, mode):
    if not message.strip():
        return "", history
    
    if mode == "🧠 Quiz Me":
        prompt = f"{SYSTEM_PROMPT}\n\nCreate a 5-question multiple choice quiz about: {message}"
    elif mode == "🃏 Flashcards":
        prompt = f"{SYSTEM_PROMPT}\n\nCreate 5 flashcards (Q&A format) about: {message}"
    elif mode == "📖 Explain":
        prompt = f"{SYSTEM_PROMPT}\n\nExplain this topic in simple, clear detail: {message}"
    else:
        prompt = f"{SYSTEM_PROMPT}\n\nAnswer this study question helpfully: {message}"

    contents = []
    for item in history:
        if item["role"] == "user":
            contents.append({"role": "user", "parts": [{"text": item["content"]}]})
        else:
            contents.append({"role": "model", "parts": [{"text": item["content"]}]})
    contents.append({"role": "user", "parts": [{"text": prompt}]})

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=contents
    )

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": response.text})
    return "", history

def clear_chat():
    return "", [{"role": "assistant", "content": "Hi! 👋 I'm your AI Study Buddy. What would you like to learn today? ✨"}]

with gr.Blocks(theme=gr.themes.Soft(primary_hue="violet")) as demo:

    gr.HTML('<h1 style="text-align:center; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2em; padding: 20px;">📚 AI Study Buddy</h1>')
    gr.HTML('<p style="text-align:center; color:#888; margin-bottom:20px;">Your personal learning assistant — ask anything!</p>')

    with gr.Row():
        mode = gr.Radio(
            choices=["💬 Ask Anything", "🧠 Quiz Me", "🃏 Flashcards", "📖 Explain"],
            value="💬 Ask Anything",
            label="Choose Mode",
        )

    chatbot = gr.Chatbot(
        value=[{"role": "assistant", "content": "Hi! 👋 I'm your AI Study Buddy. What would you like to learn today? ✨"}],
        height=450,
        show_label=False,
        
    )

    with gr.Row():
        msg = gr.Textbox(
            placeholder="Ask me anything...",
            show_label=False,
            scale=4,
            container=False,
        )
        send_btn = gr.Button("Send ➤", variant="primary", scale=1)

    clear_btn = gr.Button("🗑️ Clear Chat", variant="secondary")

    gr.Examples(
        examples=[
            ["Explain photosynthesis"],
            ["Quiz me on World War 2"],
            ["Make flashcards for the water cycle"],
            ["What is the Pythagorean theorem?"],
        ],
        inputs=msg,
        label="💡 Quick Start",
    )

    send_btn.click(chat, [msg, chatbot, mode], [msg, chatbot])
    msg.submit(chat, [msg, chatbot, mode], [msg, chatbot])
    clear_btn.click(clear_chat, [], [msg, chatbot])

demo.launch()