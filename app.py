import gradio as gr
import google.generativeai as genai

# ---------------- API ----------------
genai.configure(api_key="YOUR_GOOGLE_AI_STUDIO_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")


# ---------------- NOTES ----------------
def process_notes(text):
    if not text or text.strip() == "":
        return "Please enter notes first."

    prompt = f"""
Summarize these notes, create 5 questions, and study tips:

{text}
"""
    res = model.generate_content(prompt)
    return res.text


# ---------------- CHAT ----------------
def chat(message, history):
    history = history or []

    context = ""
    for u, b in history:
        context += f"User: {u}\nAssistant: {b}\n"

    prompt = f"""
You are a helpful tutor.

{context}

User: {message}
Assistant:
"""

    res = model.generate_content(prompt)

    history.append((message, res.text))
    return "", history


# ---------------- UI ----------------
theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="indigo",
    neutral_hue="slate"
)

with gr.Blocks(theme=theme) as app:

    # 🌈 HEADER (COLORFUL)
    gr.Markdown(
        """
        <div style="text-align:center; padding:10px;">
            <h1 style="color:#4f46e5;">📘 Study Companion</h1>
            <p style="color:#6b7280;">Simple Notes • Smart Chat • Fast Learning</p>
        </div>
        """,
        elem_id="header"
    )

    with gr.Tabs():

        # ---------------- NOTES ----------------
        with gr.Tab("📄 Notes"):

            gr.Markdown("### Paste your notes below 👇")

            inp = gr.Textbox(
                lines=10,
                placeholder="Type or paste your notes here..."
            )

            btn = gr.Button("✨ Generate", variant="primary")
            out = gr.Markdown()

            btn.click(process_notes, inp, out)


        # ---------------- CHAT ----------------
        with gr.Tab("💬 Chat"):

            gr.Markdown("### Ask anything 👇")

            chatbot = gr.Chatbot(height=500)

            msg = gr.Textbox(
                placeholder="Type your question...",
                scale=4
            )

            send = gr.Button("Send 🚀", variant="primary")

            msg.submit(chat, [msg, chatbot], [msg, chatbot])
            send.click(chat, [msg, chatbot], [msg, chatbot])


# ---------------- RUN ----------------
app.launch()