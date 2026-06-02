
import gradio as gr

def study_buddy(text):
    if not text.strip():
        return "Please enter some study material."

    words = text.split()

    summary = " ".join(words[:100])

    quiz = f"""
1. What is the main topic of the text?
2. Mention two important points from the text.
3. Explain the concept in your own words.
"""

    tips = """
📚 Study Tips:
- Revise after reading.
- Create short notes.
- Practice active recall.
- Take short breaks while studying.
"""

    return f"### Summary\n{summary}\n\n### Quiz\n{quiz}\n\n### Study Tips\n{tips}"

demo = gr.Interface(
    fn=study_buddy,
    inputs=gr.Textbox(
        lines=10,
        placeholder="Paste your study notes here..."
    ),
    outputs="markdown",
    title="AI Study Buddy",
    description="Summarize notes, generate quiz questions and get study tips."
)

if __name__ == "__main__":
    demo.launch()
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
        - Ask for help breaking down complex topics
        - Share your questions freely - no question is too simple!
        """)
        
        # Set up message handling
        def respond(user_message, history):
            bot_response = study_buddy_chat(user_message, history)
            return "", history + [[user_message, bot_response]]
        
        # Handle submit button and Enter key
        msg.submit(respond, [msg, chatbot], [msg, chatbot])
        submit_btn.click(respond, [msg, chatbot], [msg, chatbot])
    
    return demo

if __name__ == "__main__":
    # Create and launch the interface
    demo = create_interface()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )
    

