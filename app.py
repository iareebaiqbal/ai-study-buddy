import gradio as gr
import google.generativeai as genai
import os

# Gemini API Setup
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

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
    
    # Build conversation history
    chat_history = []
    for human, assistant in history:
        chat_history.append({"role": "user", "parts": [human]})
        chat_history.append({"role": "model", "parts": [assistant]})
    
    chat_session = model.start_chat(history=chat_history)
    response = chat_session.send_message(prompt)
    
    history.append((message, response.text))
    return "", history

def clear_chat():
    return [], []

# UI
with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="violet",
        secondary_hue="purple",
    ),
    css="""
    .gradio-container {
        max-width: 800px !important;
        margin: auto !important;
    }
    .chat-title {
        text-align: center;
        font-size: 2em;
        font-weight: bold;
        padding: 20px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        text-align: center;
        color: #888;
        margin-bottom: 20px;
        font-size: 1em;
    }
    """
) as demo:

    gr.HTML('<div class="chat-title">📚 AI Study Buddy</div>')
    gr.HTML('<div class="subtitle">Your personal learning assistant — ask anything!</div>')

    with gr.Row():
        mode = gr.Radio(
            choices=["💬 Ask Anything", "🧠 Quiz Me", "🃏 Flashcards", "📖 Explain"],
            value="💬 Ask Anything",
            label="Choose Mode",
        )

    chatbot = gr.Chatbot(
        value=[[None, "Hi! 👋 I'm your AI Study Buddy. What would you like to learn today? ✨"]],
        height=450,
        bubble_full_width=False,
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

    with gr.Row():
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

    # Actions
    send_btn.click(chat, [msg, chatbot, mode], [msg, chatbot])
    msg.submit(chat, [msg, chatbot, mode], [msg, chatbot])
    clear_btn.click(clear_chat, [], [msg, chatbot])

demo.launch()