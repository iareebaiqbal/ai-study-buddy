import gradio as gr
import os
import requests

# =========================
# 🔥 BACKEND FUNCTION
# =========================

def get_response(message, history):

    # 🔑 Try API first (if available)
    api_key = os.getenv("API_KEY")

    if api_key:
        try:
            url = "https://api.openai.com/v1/chat/completions"

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a helpful study assistant."},
                    {"role": "user", "content": message}
                ]
            }

            response = requests.post(url, headers=headers, json=data)
            result = response.json()

            return result["choices"][0]["message"]["content"]

        except Exception as e:
            return f"⚠ API Error: {str(e)}"

    # 🧠 Fallback (NO API)
    return fallback_bot(message)


# =========================
# 🧠 FALLBACK BOT (NO API)
# =========================

def fallback_bot(message):
    msg = message.lower()

    if "hello" in msg:
        return "Hello! 👋 I am your AI Study Buddy. How can I help?"
    elif "network" in msg:
        return "Computer Networks include LAN, WAN, routers, switches, OSI model etc."
    elif "ip" in msg:
        return "IP address is a unique identifier for devices on a network."
    elif "bye" in msg:
        return "Goodbye! Keep studying 📚"
    else:
        return "I am still learning 🤖 — please ask something else."


# =========================
# 🎨 FRONTEND UI
# =========================

custom_css = """
body {
    background: #0f172a;
    font-family: Arial;
}

.gradio-container {
    max-width: 900px !important;
    margin: auto !important;
}

/* Chat bubbles */
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

/* Input box */
textarea {
    border-radius: 10px !important;
}
"""


# =========================
# 🚀 APP LAUNCH
# =========================

with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    # 📚 AI Study Buddy
    ### Your smart learning assistant 🚀
    """)

    gr.ChatInterface(
        fn=get_response,
        title="Study Assistant",
        description="Ask me anything about Computer Science or general studies",
    )

demo.launch()