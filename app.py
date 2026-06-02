import gradio as gr
import google.generativeai as genai

# ---------------- API ----------------
genai.configure(api_key="YOUR_GOOGLE_AI_STUDIO_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")


# ---------------- NOTES ----------------
def process_notes(text):
    if not text:
        return "Please enter notes first."

    prompt = f"""
Summarize, give 5 questions and study tips:

{text}
"""
    try:
        res = model.generate_content(prompt)
        return res.text
    except Exception as e:
        return f"Error: {str(e)}"


# ---------------- CHAT ----------------
def chat(message, history):
    if history is None:
        history = []

    context = ""
    for u, b in history:
        context += f"User: {u}\nAI: {b}\n"

    prompt = f"""
You are a study assistant.

{context}

User: {message}
AI:
"""

    try:
        res = model.generate_content(prompt)
        reply = res.text
    except Exception as e:
        reply = f"Error: {str(e)}"

    history.append((message, reply))
    return "", history


# ---------------- UI ----------------
with gr.Blocks() as app:

    gr.Markdown("# Study Companion")

    with gr.Tabs():

        with gr.Tab("Notes"):
            inp = gr.Textbox(lines=10, placeholder="Paste notes here")
            btn = gr.Button("Generate")
            out = gr.Markdown()

            btn.click(process_notes, inp, out)

        with gr.Tab("Chat"):
            chatbot = gr.Chatbot(height=500)

            msg = gr.Textbox(placeholder="Ask question")
            send = gr.Button("Send")

            msg.submit(chat, [msg, chatbot], [msg, chatbot])
            send.click(chat, [msg, chatbot], [msg, chatbot])


app.launch()

    