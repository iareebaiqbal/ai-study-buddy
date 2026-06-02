import gradio as gr
import google.generativeai as genai

# -----------------------------
# CONFIGURE GEMINI
# -----------------------------
API_KEY = "YOUR_GOOGLE_AI_STUDIO_KEY"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


# -----------------------------
# 1. NOTES ANALYZER (AI)
# -----------------------------
def study_buddy(notes):
    prompt = f"""
You are an expert study assistant.

From the following notes:
1. Create a short summary
2. Generate 5 quiz questions
3. Give study tips

NOTES:
{notes}
"""

    response = model.generate_content(prompt)
    return response.text


# -----------------------------
# 2. CHAT FUNCTION (AI + MEMORY)
# -----------------------------
def study_buddy_chat(message, history):
    history_text = ""

    for user, bot in history:
        history_text += f"User: {user}\nAI: {bot}\n"

    prompt = f"""
You are a helpful AI tutor.

Conversation so far:
{history_text}

User: {message}
AI:
"""

    response = model.generate_content(prompt)

    history.append((message, response.text))
    return "", history


# -----------------------------
# 3. UI (GRADIO ADVANCED)
# -----------------------------
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("# 🎓 AI Study Buddy (Gemini Powered)")
    gr.Markdown("Next-level AI for summaries, quizzes, and chat 🚀")

    with gr.Tabs():

        # ---------------- NOTES TAB ----------------
        with gr.Tab("📄 Notes Analyzer"):

            notes_input = gr.Textbox(
                label="Paste your notes",
                lines=10,
                placeholder="Write or paste your study material..."
            )

            btn = gr.Button("Generate", variant="primary")
            output = gr.Markdown()

            btn.click(study_buddy, inputs=notes_input, outputs=output)


        # ---------------- CHAT TAB ----------------
        with gr.Tab("💬 AI Tutor Chat"):

            chatbot = gr.Chatbot(height=450)

            msg = gr.Textbox(
                placeholder="Ask your question...",
                scale=4
            )

            send = gr.Button("Send", variant="primary")

            def respond(message, history):
                return study_buddy_chat(message, history)

            msg.submit(respond, [msg, chatbot], [msg, chatbot])
            send.click(respond, [msg, chatbot], [msg, chatbot])


    gr.Markdown("⚡ Powered by Google Gemini API")


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    demo.launch()