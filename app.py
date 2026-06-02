import gradio as gr

def respond(user_message, history):
    bot_response = study_buddy_chat(user_message, history)
    history = history + [[user_message, bot_response]]
    return "", history


with gr.Blocks() as demo:
    gr.Markdown("# AI Study Buddy")

    chatbot = gr.Chatbot(
        label="Study Chat",
        type="messages",
        height=500
    )

    with gr.Row():
        msg = gr.Textbox(
            label="Your Question",
            placeholder="Ask me anything about your studies...",
            lines=2,
            scale=4
        )
        submit_btn = gr.Button("Send", scale=1, variant="primary")

    gr.Markdown("""
    ### Tips:
    - Ask for explanations of difficult concepts  
    - Request study strategies and learning tips  
    - Break complex topics into simple parts  
    """)

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    submit_btn.click(respond, [msg, chatbot], [msg, chatbot])


if __name__ == "__main__":
    demo.launch()
