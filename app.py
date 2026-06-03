import gradio as gr
import os
from huggingface_hub import InferenceClient

=========================

🔥 BACKEND FUNCTION

=========================

client = InferenceClient(
model="mistralai/Mistral-7B-Instruct-v0.3",
token=os.getenv("API_Key")
)

def get_response(message, history):
try:
messages = [
{"role": "system", "content": """You are an expert AI Study Buddy 📚.
Help students with Computer Science, Math, Physics, and all subjects.
Give clear, simple, and detailed explanations.
Use examples where possible. Be friendly and encouraging! 🌟"""}
]

# Add history  
    for user_msg, bot_msg in history:  
        messages.append({"role": "user", "content": user_msg})  
        messages.append({"role": "assistant", "content": bot_msg})  
      
    messages.append({"role": "user", "content": message})  
      
    response = client.chat_completion(  
        messages=messages,  
        max_tokens=1024,  
        temperature=0.7  
    )  
      
    return response.choices[0].message.content  
      
except Exception as e:  
    return fallback_bot(message)

=========================

🧠 FALLBACK BOT (NO API)

=========================

def fallback_bot(message):
msg = message.lower()

if any(w in msg for w in ["hello", "hi", "hey"]):  
    return "Hello! 👋 I am your AI Study Buddy. Ask me anything about your studies!"  
elif "network" in msg:  
    return "🌐 Computer Networks include LAN, WAN, routers, switches, OSI model etc."  
elif "ip" in msg:  
    return "🔢 IP address is a unique identifier for devices on a network. IPv4 has 4 octets (e.g., 192.168.1.1)"  
elif "python" in msg:  
    return "🐍 Python is a high-level programming language known for simplicity and versatility!"  
elif "oop" in msg or "object" in msg:  
    return "🏗️ OOP has 4 pillars: Encapsulation, Inheritance, Polymorphism, Abstraction!"  
elif "os" in msg or "operating system" in msg:  
    return "💻 Operating System manages hardware & software resources. Examples: Windows, Linux, MacOS"  
elif "database" in msg or "sql" in msg:  
    return "🗄️ Database stores organized data. SQL is used to query relational databases like MySQL!"  
elif "bye" in msg or "thanks" in msg:  
    return "Goodbye! Keep studying hard! You got this! 💪📚"  
else:  
    return "🤔 Interesting question! Try asking about: Python, Networks, OOP, OS, Database, or any CS topic!"

=========================

🎨 FRONTEND UI

=========================

custom_css = """
body {
background: #0f172a;
font-family: Arial;
}

.gradio-container {
max-width: 900px !important;
margin: auto !important;
}

.message.user {
background-color: #2563eb !important;
color: white !important;
border-radius: 15px !important;
}

.message.bot {
background-color: #1e293b !important;
color: white !important;
border-radius: 15px !important;
}

textarea {
border-radius: 10px !important;
}
"""

=========================

🚀 APP LAUNCH

=========================

with gr.Blocks() as demo:

gr.Markdown("""  
# 📚 AI Study Buddy  
### Your smart learning assistant 🚀  
""")  

gr.ChatInterface(  
    fn=get_response,  
    title="Study Assistant",  
    description="Ask me anything about Computer Science or general studies",  
)

demo.launch(css=custom_css, theme=gr.themes.Soft())