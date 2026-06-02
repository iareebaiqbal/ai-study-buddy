import gradio as gr
import anthropic
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Anthropic client
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def study_buddy_chat(message, chat_history):
    """
    Main chat function for AI Study Buddy.
    Takes user message and returns AI response with study assistance.
    """
    
    # Build conversation history for context
    messages = []
    for user_msg, assistant_msg in chat_history:
        messages.append({"role": "user", "content": user_msg})
        if assistant_msg:
            messages.append({"role": "assistant", "content": assistant_msg})
    
    # Add current message
    messages.append({"role": "user", "content": message})
    
    try:
        # Call Claude API
        response = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=1024,
            system="""You are an AI Study Buddy - a helpful educational assistant designed to help learners understand concepts, 
solve problems, and improve their learning. 

Your responsibilities:
1. Explain complex concepts in simple, clear language
2. Provide study tips and learning strategies
3. Help break down problems into manageable steps
4. Ask clarifying questions to check understanding
5. Encourage critical thinking rather than just giving answers
6. Provide examples and analogies to help with understanding
7. Be patient, supportive, and motivating

Always adapt your explanation style to the learner's level and be encouraging!""",
            messages=messages
        )
        
        return response.content[0].text
    
    except Exception as e:
        return f"Error: {str(e)}"

def create_interface():
    """Create and configure the Gradio interface"""
    
    with gr.Blocks(title="AI Study Buddy", theme=gr.themes.Soft()) as demo:
        gr.Markdown("""
        # 🎓 AI Study Buddy
        Your personal AI-powered learning companion
        
        Ask me anything about your studies - I'm here to help you learn and grow!
        """)
        
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
    

