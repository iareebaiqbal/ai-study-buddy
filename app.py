import gradio as gr
import google.generativeai as genai

# -----------------------
# CONFIG
# -----------------------
API_KEY = "YOUR_GOOGLE_AI_STUDIO_KEY"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


# -----------------------
# NOTES FUNCTION
# -----------------------
def process_notes(text):
    prompt = f"""
Summarize the notes, create 5 questions, and give study tips:

{text}
"""
    res = model.generate_content(prompt)
    return res.text


# -----------------------
# CHAT FUNCTION
# -----------------------
def chat(msg, history):
    history = history or []

    chat_log = ""
    for u, b in history:
        chat_log += f"User: {u}\nBot: {b}\n"

    prompt = f"""
Conversation:
{chat_log}

User: {msg}
Bot:
"""

    res = model.generate_content(prompt)

    history.append((msg, res.text))
    return "", history


# -----------------------
# UI
# -----------------------
with gr.Blocks() as app:

    gr.Markdown("# Study Companion")

    with gr.Tabs():

        # -------- NOTES --------
        with gr.Tab("Notes"):
            inp = gr.Textbox(lines=10, placeholder="Paste notes here")
            out = gr.Markdown()
            btn = gr.Button("Run")

            btn.click(process_notes, inp, out)

        # -------- CHAT --------
        with gr.Tab("Chat"):
            box = gr.Chatbot(height=450)

            msg = gr.Textbox(placeholder="Ask something...")
            send = gr.Button("Send")

            msg.submit(chat, [msg, box], [msg, box])
            send.click(chat, [msg, box], [msg, box])


# -----------------------
# RUN
# -----------------------
app.launch()