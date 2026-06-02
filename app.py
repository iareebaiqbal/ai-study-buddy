import gradio as gr
import google.generativeai as genai

# -----------------------
# API SETUP
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
# CHAT FUNCTION (FIXED)
# -----------------------
def chat(message, history):
    history = history or []

    context = ""
    for user, bot in history:
        context += f"User: {user}\nAssistant: {bot}\n"

    prompt = f"""
You are a helpful study assistant.

Conversation:
{context}

User: {message}
Assistant:
"""

    response = model.generate_content(prompt)

    history.append((message, response.text))
    return "", history


# -----------------------
# UI DESIGN
# -----------------------
theme = gr.themes.Soft()

with gr.Blocks(theme=theme) as app:

    gr.Markdown("# 📘 Study Companion")
    gr.Markdown("Notes + Chat assistant")

    with gr.Tabs():

        # ---------------- NOTES TAB ----------------
        with gr.Tab("Notes"):
            notes_input = gr.Textbox(
                lines=10,
                placeholder="Paste your study notes here..."
            )

            btn = gr.Button("Generate", variant="primary")
            output = gr.Markdown()

            btn.click(process_notes, notes_input, output)


        # ---------------- CHAT TAB ----------------
        with gr.Tab("Chat"):
            chatbot = gr.Chatbot(height=500)

            msg = gr.Textbox(placeholder="Ask your question...")
            send = gr.Button("Send", variant="primary")

            def respond(message, history):
                return chat(message, history)

            msg.submit(respond, [msg, chatbot], [msg, chatbot])
            send.click(respond, [msg, chatbot], [msg, chatbot])


# -----------------------
# RUN APP
# -----------------------
if __name__ == "__main__":
    app.launch()