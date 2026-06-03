<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Study Buddy</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

  * { margin: 0; padding: 0; box-sizing: border-box; }

  :root {
    --bg: #0d1117;
    --surface: #161b22;
    --surface2: #21262d;
    --accent: #7c3aed;
    --accent2: #a78bfa;
    --text: #e6edf3;
    --muted: #8b949e;
    --user-bubble: #7c3aed;
    --bot-bubble: #21262d;
    --border: #30363d;
  }

  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--bg);
    color: var(--text);
    height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  /* Header */
  .header {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 14px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
    flex-shrink: 0;
  }

  .header-icon {
    font-size: 28px;
  }

  .header-info h1 {
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 800;
    color: var(--text);
  }

  .header-info p {
    font-size: 12px;
    color: var(--accent2);
    font-weight: 300;
  }

  .status-dot {
    width: 8px;
    height: 8px;
    background: #3fb950;
    border-radius: 50%;
    margin-left: auto;
    box-shadow: 0 0 6px #3fb950;
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
  }

  /* API Key Input */
  .api-setup {
    background: var(--surface2);
    border-bottom: 1px solid var(--border);
    padding: 10px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
  }

  .api-setup input {
    flex: 1;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 7px 12px;
    color: var(--text);
    font-size: 12px;
    font-family: 'DM Sans', sans-serif;
    outline: none;
  }

  .api-setup input:focus {
    border-color: var(--accent);
  }

  .api-setup input::placeholder {
    color: var(--muted);
  }

  .api-label {
    font-size: 11px;
    color: var(--muted);
    white-space: nowrap;
  }

  /* Chat Area */
  .chat-area {
    flex: 1;
    overflow-y: auto;
    padding: 20px 16px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    scroll-behavior: smooth;
  }

  .chat-area::-webkit-scrollbar { width: 4px; }
  .chat-area::-webkit-scrollbar-track { background: transparent; }
  .chat-area::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }

  /* Welcome */
  .welcome {
    text-align: center;
    padding: 30px 10px;
  }

  .welcome h2 {
    font-family: 'Syne', sans-serif;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 8px;
    background: linear-gradient(135deg, var(--accent2), #f0abfc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .welcome p {
    color: var(--muted);
    font-size: 13px;
    margin-bottom: 20px;
  }

  .chips {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
  }

  .chip {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 12px;
    color: var(--accent2);
    cursor: pointer;
    transition: all 0.2s;
  }

  .chip:hover {
    background: var(--accent);
    border-color: var(--accent);
    color: white;
    transform: translateY(-1px);
  }

  /* Messages */
  .message {
    display: flex;
    gap: 10px;
    animation: fadeIn 0.3s ease;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .message.user {
    flex-direction: row-reverse;
  }

  .avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
    background: var(--surface2);
    border: 1px solid var(--border);
  }

  .message.user .avatar {
    background: var(--accent);
    border-color: var(--accent);
  }

  .bubble {
    max-width: 80%;
    padding: 12px 16px;
    border-radius: 16px;
    font-size: 14px;
    line-height: 1.6;
  }

  .message.bot .bubble {
    background: var(--bot-bubble);
    border: 1px solid var(--border);
    border-top-left-radius: 4px;
    color: var(--text);
  }

  .message.user .bubble {
    background: var(--user-bubble);
    border-top-right-radius: 4px;
    color: white;
  }

  /* Typing indicator */
  .typing .bubble {
    display: flex;
    gap: 5px;
    align-items: center;
    padding: 14px 18px;
  }

  .dot {
    width: 7px;
    height: 7px;
    background: var(--muted);
    border-radius: 50%;
    animation: bounce 1.2s infinite;
  }

  .dot:nth-child(2) { animation-delay: 0.2s; }
  .dot:nth-child(3) { animation-delay: 0.4s; }

  @keyframes bounce {
    0%, 60%, 100% { transform: translateY(0); }
    30% { transform: translateY(-6px); }
  }

  /* Input Area */
  .input-area {
    background: var(--surface);
    border-top: 1px solid var(--border);
    padding: 12px 16px;
    display: flex;
    gap: 10px;
    align-items: flex-end;
    flex-shrink: 0;
  }

  .input-wrap {
    flex: 1;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 12px;
    display: flex;
    align-items: center;
    padding: 0 12px;
    transition: border-color 0.2s;
  }

  .input-wrap:focus-within {
    border-color: var(--accent);
  }

  textarea {
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    padding: 12px 0;
    resize: none;
    max-height: 120px;
    overflow-y: auto;
  }

  textarea::placeholder { color: var(--muted); }

  .send-btn {
    width: 42px;
    height: 42px;
    background: var(--accent);
    border: none;
    border-radius: 10px;
    color: white;
    font-size: 18px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
    flex-shrink: 0;
  }

  .send-btn:hover { background: #6d28d9; transform: scale(1.05); }
  .send-btn:disabled { background: var(--surface2); color: var(--muted); cursor: not-allowed; transform: none; }

  /* Error */
  .error-msg {
    background: #2d1b1b;
    border: 1px solid #f85149;
    color: #f85149;
    padding: 10px 14px;
    border-radius: 10px;
    font-size: 13px;
    text-align: center;
  }
</style>
</head>
<body>

<div class="header">
  <div class="header-icon">📚</div>
  <div class="header-info">
    <h1>AI Study Buddy</h1>
    <p>Your smart learning assistant 🚀</p>
  </div>
  <div class="status-dot"></div>
</div>

<div class="api-setup">
  <span class="api-label">HF Token:</span>
  <input type="password" id="hfToken" placeholder="hf_xxxxxxxxxxxxxxxxxxxxxxxx (optional for some models)" />
</div>

<div class="chat-area" id="chatArea">
  <div class="welcome">
    <h2>Study Assistant</h2>
    <p>Ask me anything — any subject, any topic!</p>
    <div class="chips">
      <div class="chip" onclick="sendChip(this)">🐍 Python</div>
      <div class="chip" onclick="sendChip(this)">🌐 Networks</div>
      <div class="chip" onclick="sendChip(this)">🗄️ Database</div>
      <div class="chip" onclick="sendChip(this)">🧮 Math</div>
      <div class="chip" onclick="sendChip(this)">⚙️ OOP</div>
      <div class="chip" onclick="sendChip(this)">🧠 AI/ML</div>
      <div class="chip" onclick="sendChip(this)">📐 Physics</div>
      <div class="chip" onclick="sendChip(this)">💡 Any Topic</div>
    </div>
  </div>
</div>

<div class="input-area">
  <div class="input-wrap">
    <textarea id="userInput" placeholder="Koi bhi question poochein..." rows="1"
      onkeydown="handleKey(event)" oninput="autoResize(this)"></textarea>
  </div>
  <button class="send-btn" id="sendBtn" onclick="sendMessage()">➤</button>
</div>

<script>
  let isLoading = false;

  const MODELS = [
    "mistralai/Mistral-7B-Instruct-v0.3",
    "HuggingFaceH4/zephyr-7b-beta",
    "microsoft/Phi-3-mini-4k-instruct"
  ];

  function autoResize(el) {
    el.style.height = 'auto';
    el.style.height = Math.min(el.scrollHeight, 120) + 'px';
  }

  function handleKey(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  }

  function sendChip(el) {
    const text = el.textContent.replace(/[^\w\s]/g, '').trim();
    document.getElementById('userInput').value = `Tell me about ${text}`;
    sendMessage();
  }

  function addMessage(role, text) {
    const chatArea = document.getElementById('chatArea');

    // Remove welcome on first message
    const welcome = chatArea.querySelector('.welcome');
    if (welcome) welcome.remove();

    const div = document.createElement('div');
    div.className = `message ${role}`;

    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.textContent = role === 'user' ? '👤' : '🤖';

    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.innerHTML = text.replace(/\n/g, '<br>');

    div.appendChild(avatar);
    div.appendChild(bubble);
    chatArea.appendChild(div);
    chatArea.scrollTop = chatArea.scrollHeight;
    return div;
  }

  function addTyping() {
    const chatArea = document.getElementById('chatArea');
    const div = document.createElement('div');
    div.className = 'message bot typing';
    div.id = 'typingIndicator';
    div.innerHTML = `
      <div class="avatar">🤖</div>
      <div class="bubble">
        <div class="dot"></div><div class="dot"></div><div class="dot"></div>
      </div>`;
    chatArea.appendChild(div);
    chatArea.scrollTop = chatArea.scrollHeight;
  }

  function removeTyping() {
    const el = document.getElementById('typingIndicator');
    if (el) el.remove();
  }

  async function queryHF(userMessage, token) {
    const prompt = `<s>[INST] You are a helpful study assistant. Answer clearly and thoroughly about any topic — not just CS. Be educational and easy to understand.

Question: ${userMessage} [/INST]`;

    const headers = { 'Content-Type': 'application/json' };
    if (token) headers['Authorization'] = `Bearer ${token}`;

    // Try each model
    for (const model of MODELS) {
      try {
        const res = await fetch(`https://api-inference.huggingface.co/models/${model}`, {
          method: 'POST',
          headers,
          body: JSON.stringify({
            inputs: prompt,
            parameters: {
              max_new_tokens: 500,
              temperature: 0.7,
              return_full_text: false
            }
          })
        });

        if (!res.ok) continue;
        const data = await res.json();

        if (data.error && data.error.includes('loading')) {
          return `⏳ Model is loading, please wait 20 seconds and try again.`;
        }

        if (Array.isArray(data) && data[0]?.generated_text) {
          return data[0].generated_text.trim();
        }
      } catch (e) {
        continue;
      }
    }

    return "❌ Could not get response. Please add your HF Token above for better access, or try again.";
  }

  async function sendMessage() {
    if (isLoading) return;
    const input = document.getElementById('userInput');
    const text = input.value.trim();
    if (!text) return;

    const token = document.getElementById('hfToken').value.trim();

    isLoading = true;
    document.getElementById('sendBtn').disabled = true;
    input.value = '';
    input.style.height = 'auto';

    addMessage('user', text);
    addTyping();

    const reply = await queryHF(text, token);
    removeTyping();
    addMessage('bot', reply);

    isLoading = false;
    document.getElementById('sendBtn').disabled = false;
    input.focus();
  }
</script>
</body>
</html>