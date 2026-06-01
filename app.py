import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Free local model - no cloud API needed!
MODEL_NAME = "google/flan-t5-base"

print("Loading model... please wait!")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
print("Model loaded!")

AGENT_TRACE = []

SYSTEM_PREFIX = """You are a friendly AI Study Buddy. Help students learn by explaining concepts clearly, making quizzes, and creating flashcards. Be encouraging and use simple language.\n\n"""

def get_mode_prompt(message, mode):
    if mode == "🧠 Quiz Me":
        return f"Create 5 multiple choice quiz questions about: {message}. Format: Q1. question a) b) c) d) Answer:"
    elif mode == "🃏 Flashcards":
        return f"Create 5 study flashcards about: {message}. Format: Flashcard 1 Front: Back:"
    elif mode == "📖 Explain":
        return f"Explain this topic in simple easy language with an example: {message}"
    return f"Answer this study question helpfully: {message}"

def chat(message, history, mode):
    AGENT_TRACE.append(f"[INPUT] Mode: {mode} | Message: {message}")

    prompt = SYSTEM_PREFIX + get_mode_prompt(message, mode)
    AGENT_TRACE.append(f"[PROMPT] {prompt[:100]}...")
    AGENT_TRACE.append(f"[MODEL] Running flan-t5-base locally (no cloud API!)")

    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            temperature=0.7,
            do_sample=True,
            top_p=0.9,
            repetition_penalty=1.2,
        )
    
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    AGENT_TRACE.append(f"[RESPONSE] {len(reply)} characters generated locally")
    return reply

def get_trace():
    if not AGENT_TRACE:
        return "No trace yet — ask a question first!"
    return "\n\n".join(AGENT_TRACE)

css = """
body { font-family: 'Georgia', serif; }
.gradio-container { 
    background: linear-gradient(145deg, #fff5f7 0%, #fef9f0 40%, #f0f4ff 100%) !important;
}
footer { display: none !important; }
"""

with gr.Blocks(title="AI Study Buddy", css=css, theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    # 📚 AI Study Buddy
    ### *your cozy corner for learning ✨*
    > 🏆 **Gradio Build-Small Hackathon 2026** — by **Areeba Iqbal**
    > 
    > 🔌 **Off the Grid** — Running 100% locally, no cloud APIs!
    """)

    with gr.Row():
        mode = gr.Radio(
            choices=["💬 Ask Anything", "🧠 Quiz Me", "🃏 Flashcards", "📖 Explain"],
            value="💬 Ask Anything",
            label="🎯 Choose Mode",
            interactive=True,
        )

    with gr.Tabs():
        with gr.Tab("💬 Chat"):
            chatbot = gr.Chatbot(
                value=[[None, "Hi there! 🌸 I'm your AI Study Buddy! Ask me anything — I can explain concepts, quiz you, or make flashcards. What shall we learn today? ✨"]],
                height=450,
                label="AI Study Buddy",
                bubble_full_width=False,
            )
            with gr.Row():
                txt = gr.Textbox(
                    placeholder="Ask me anything... 🌸",
                    label="",
                    scale=5,
                    lines=1,
                )
                send_btn = gr.Button("➤ Send", scale=1, variant="primary")
                clear_btn = gr.Button("🗑️ Clear", scale=1)

            gr.Examples(
                examples=[
                    "Explain photosynthesis",
                    "Quiz me on World War 2",
                    "Flashcards for Newton's Laws",
                    "What is machine learning?",
                    "Summarize the water cycle",
                ],
                inputs=txt,
                label="💡 Quick Start",
            )

        with gr.Tab("🔍 Agent Trace"):
            gr.Markdown("### See how AI Study Buddy thinks — step by step!")
            gr.Markdown("**Sharing is Caring** quest ✅ — full agent trace visible here!")
            trace_box = gr.Textbox(
                label="Agent Trace Log",
                lines=15,
                interactive=False,
                placeholder="Ask a question first, then come here to see the trace!",
            )
            refresh_btn = gr.Button("🔄 Refresh Trace", variant="secondary")
            refresh_btn.click(fn=get_trace, outputs=trace_box)

    def respond(message, history, mode_val):
        if not message.strip():
            return history, ""
        reply = chat(message, history, mode_val)
        history.append((message, reply))
        return history, ""

    def clear():
        AGENT_TRACE.clear()
        return [[None, "Chat cleared! 🌸 What would you like to study next?"]], ""

    send_btn.click(respond, [txt, chatbot, mode], [chatbot, txt])
    txt.submit(respond, [txt, chatbot, mode], [chatbot, txt])
    clear_btn.click(clear, outputs=[chatbot, txt])

    gr.Markdown("""
    ---
    Made with 🌸 by **Areeba Iqbal** · AI Study Buddy · Gradio Build-Small Hackathon 2026
    """)

demo.launch()
