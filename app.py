import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "google/flan-t5-base"

print("Loading model... please wait!")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME, low_cpu_mem_usage=True)
print("Model loaded!")

AGENT_TRACE = []

SYSTEM_PREFIX = "You are a friendly AI Study Buddy. Help students learn clearly.\n\n"

def get_mode_prompt(message, mode):
    if mode == "🧠 Quiz Me":
        return f"Create 5 multiple choice quiz questions about: {message}."
    elif mode == "🃏 Flashcards":
        return f"Create 5 study flashcards about: {message}."
    elif mode == "📖 Explain":
        return f"Explain this topic simply with an example: {message}"
    return f"Answer this study question: {message}"

def chat(message, history, mode):
    AGENT_TRACE.append(f"[INPUT] Mode: {mode} | Message: {message}")
    prompt = SYSTEM_PREFIX + get_mode_prompt(message, mode)
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.7,
            do_sample=True,
            top_p=0.9,
            repetition_penalty=1.2,
        )
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    AGENT_TRACE.append(f"[RESPONSE] {len(reply)} characters generated")
    return reply

def get_trace():
    if not AGENT_TRACE:
        return "No trace yet — ask a question first!"
    return "\n\n".join(AGENT_TRACE)

with gr.Blocks(title="AI Study Buddy", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 📚 AI Study Buddy
    ### *your cozy corner for learning ✨*
    > 🏆 **Gradio Build-Small Hackathon 2026** — by **Areeba Iqbal**
    """)

    mode = gr.Radio(
        choices=["💬 Ask Anything", "🧠 Quiz Me", "🃏 Flashcards", "📖 Explain"],
        value="💬 Ask Anything",
        label="🎯 Choose Mode",
    )

    with gr.Tabs():
        with gr.Tab("💬 Chat"):
            chatbot = gr.Chatbot(
                value=[{"role": "assistant", "content": "Hi there! 🌸 I'm your AI Study Buddy! What shall we learn today? ✨"}],
                height=450,
                label="AI Study Buddy",
        
            )
            with gr.Row():
                txt = gr.Textbox(placeholder="Ask me anything... 🌸", label="", scale=5)
                send_btn = gr.Button("➤ Send", scale=1, variant="primary")
                clear_btn = gr.Button("🗑️ Clear", scale=1)

            gr.Examples(
                examples=["Explain photosynthesis", "Quiz me on World War 2", "Flashcards for Newton's Laws"],
                inputs=txt,
                label="💡 Quick Start",
            )

        with gr.Tab("🔍 Agent Trace"):
            gr.Markdown("### See how AI Study Buddy thinks!")
            trace_box = gr.Textbox(label="Agent Trace Log", lines=15, interactive=False)
            refresh_btn = gr.Button("🔄 Refresh Trace", variant="secondary")
            refresh_btn.click(fn=get_trace, outputs=trace_box)

    def respond(message, history, mode_val):
        if not message.strip():
            return history, ""
        reply = chat(message, history, mode_val)
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": reply})
        return history, ""

    def clear():
        AGENT_TRACE.clear()
        return [{"role": "assistant", "content": "Chat cleared! 🌸 What would you like to study next?"}], ""

    send_btn.click(respond, [txt, chatbot, mode], [chatbot, txt])
    txt.submit(respond, [txt, chatbot, mode], [chatbot, txt])
    clear_btn.click(clear, outputs=[chatbot, txt])

    gr.Markdown("---\nMade with 🌸 by **Areeba Iqbal** · AI Study Buddy · Gradio Build-Small Hackathon 2026")

demo.launch()


