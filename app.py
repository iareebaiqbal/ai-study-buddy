import { useState, useRef, useEffect } from "react";

const SYSTEM_PROMPT ='You are an AI Study Buddy' a friendly, warm, and encouraging study assistant. Help students learn better.

You can:
1. Explain concepts in simple, easy-to-understand language
2. Generate quiz questions on any topic
3. Create flashcards (Q&A format)
4. Summarize notes or topics
5. Answer study-related questions

Always be warm, encouraging, and supportive. Use emojis occasionally to keep things fun 

Format quizzes like:
Q1. [Question]
a) option  b) option  c) option  d) option
✅ Answer: [correct]

Format flashcards like:
🃏 Flashcard 1
Front: [concept]
Back: [explanation]`;

const THEMES = {
  pinterest: {
    name: "🌸 Pinterest",
    pageBackground: "linear-gradient(145deg, #fff5f7 0%, #fef9f0 40%, #f0f4ff 100%)",
    blob1: "#ffd6e0",
    blob2: "#d4e8ff",
    cardBg: "rgba(255,255,255,0.82)",
    cardBorder: "rgba(255,200,200,0.3)",
    cardShadow: "0 8px 40px rgba(255,143,171,0.12), 0 2px 8px rgba(0,0,0,0.06)",
    titleColor: "#3d2c2c",
    subtitleColor: "#a07070",
    badgeBg: "linear-gradient(135deg, #ff8fab, #ffb347)",
    badgeColor: "#fff",
    pillActive: "linear-gradient(135deg, #ff8fab, #ffb347)",
    pillActiveShadow: "0 4px 16px rgba(255,143,171,0.4)",
    pillInactive: "rgba(255,255,255,0.8)",
    pillInactiveColor: "#8a6060",
    avatarBg: "linear-gradient(135deg, #ff8fab, #ffb347)",
    avatarShadow: "0 2px 8px rgba(255,143,171,0.35)",
    userMsgBg: "linear-gradient(135deg, #ff8fab, #ffb347)",
    userMsgColor: "#fff",
    userMsgShadow: "0 4px 16px rgba(255,143,171,0.35)",
    aiBubbleBg: "#fff",
    aiBubbleColor: "#4a3030",
    aiBubbleShadow: "0 2px 12px rgba(0,0,0,0.07)",
    aiBubbleBorder: "1.5px solid rgba(255,200,200,0.2)",
    dotBg: "linear-gradient(135deg, #ff8fab, #ffb347)",
    hintBg: "linear-gradient(90deg, #fff5f7, #fef9f0)",
    hintColor: "#c4a0a0",
    hintBorder: "rgba(255,200,200,0.2)",
    inputBg: "#fff5f7",
    inputBorder: "rgba(255,143,171,0.25)",
    inputColor: "#4a3030",
    inputPlaceholder: "#d4a0a0",
    sendBg: "linear-gradient(135deg, #ff8fab, #ffb347)",
    sendShadow: "0 4px 14px rgba(255,143,171,0.4)",
    clearBg: "#fff5f7",
    clearBorder: "rgba(255,143,171,0.2)",
    clearColor: "#c4a0a0",
    footerColor: "#c4a0a0",
    authorColor: "#e8627a",
    traceHeaderColor: "#e8627a",
    traceBg: "linear-gradient(135deg, #fff5f7, #fef9f0)",
    traceCardBg: "#fff",
    traceCardBorder: "#ff8fab",
    traceStepColor: "#e8627a",
    traceDetailColor: "#7a5c5c",
    traceTimeColor: "#c4a0a0",
    suggBg: "#fff5f7",
    suggBorder: "rgba(255,143,171,0.3)",
    suggColor: "#c07080",
    inputAreaBg: "rgba(255,255,255,0.6)",
    inputAreaBorder: "rgba(255,200,200,0.2)",
    scrollThumb: "rgba(255,143,171,0.3)",
    font: "'Palatino Linotype', Georgia, serif",
  },
  galaxy: {
    name: "🌌 Galaxy",
    pageBackground: "linear-gradient(135deg, #0f0c29, #302b63, #24243e)",
    blob1: "transparent",
    blob2: "transparent",
    cardBg: "rgba(255,255,255,0.05)",
    cardBorder: "rgba(255,255,255,0.1)",
    cardShadow: "0 25px 60px rgba(0,0,0,0.4)",
    titleColor: "#fff",
    subtitleColor: "#a0aec0",
    badgeBg: "rgba(249,199,79,0.15)",
    badgeColor: "#f9c74f",
    pillActive: "linear-gradient(135deg, #f9c74f, #f3722c)",
    pillActiveShadow: "0 4px 16px rgba(249,199,79,0.3)",
    pillInactive: "rgba(255,255,255,0.07)",
    pillInactiveColor: "#a0aec0",
    avatarBg: "linear-gradient(135deg, #f9c74f, #f3722c)",
    avatarShadow: "0 2px 8px rgba(249,199,79,0.3)",
    userMsgBg: "linear-gradient(135deg, #f9c74f, #f8961e)",
    userMsgColor: "#1a1a2e",
    userMsgShadow: "none",
    aiBubbleBg: "rgba(255,255,255,0.08)",
    aiBubbleColor: "#e2e8f0",
    aiBubbleShadow: "none",
    aiBubbleBorder: "1px solid rgba(255,255,255,0.1)",
    dotBg: "#f9c74f",
    hintBg: "rgba(249,199,79,0.05)",
    hintColor: "#718096",
    hintBorder: "rgba(255,255,255,0.06)",
    inputBg: "rgba(255,255,255,0.08)",
    inputBorder: "rgba(255,255,255,0.15)",
    inputColor: "#e2e8f0",
    inputPlaceholder: "#4a5568",
    sendBg: "linear-gradient(135deg, #f9c74f, #f3722c)",
    sendShadow: "none",
    clearBg: "rgba(255,255,255,0.05)",
    clearBorder: "rgba(255,255,255,0.15)",
    clearColor: "#718096",
    footerColor: "#4a5568",
    authorColor: "#f9c74f",
    traceHeaderColor: "#f9c74f",
    traceBg: "rgba(0,0,0,0.3)",
    traceCardBg: "rgba(249,199,79,0.08)",
    traceCardBorder: "#f9c74f",
    traceStepColor: "#f9c74f",
    traceDetailColor: "#cbd5e0",
    traceTimeColor: "#4a5568",
    suggBg: "rgba(249,199,79,0.08)",
    suggBorder: "rgba(249,199,79,0.2)",
    suggColor: "#f9c74f",
    inputAreaBg: "rgba(0,0,0,0.15)",
    inputAreaBorder: "rgba(255,255,255,0.08)",
    scrollThumb: "rgba(249,199,79,0.3)",
    font: "'Georgia', serif",
  },
  matcha: {
    name: "🍵 Matcha",
    pageBackground: "linear-gradient(145deg, #f0f7f0 0%, #e8f5e9 50%, #f5f0e8 100%)",
    blob1: "#c8e6c9",
    blob2: "#dcedc8",
    cardBg: "rgba(255,255,255,0.85)",
    cardBorder: "rgba(150,210,150,0.3)",
    cardShadow: "0 8px 40px rgba(100,180,100,0.1), 0 2px 8px rgba(0,0,0,0.05)",
    titleColor: "#2d4a2d",
    subtitleColor: "#6a9a6a",
    badgeBg: "linear-gradient(135deg, #81c784, #aed581)",
    badgeColor: "#fff",
    pillActive: "linear-gradient(135deg, #66bb6a, #aed581)",
    pillActiveShadow: "0 4px 16px rgba(102,187,106,0.35)",
    pillInactive: "rgba(255,255,255,0.85)",
    pillInactiveColor: "#5a8a5a",
    avatarBg: "linear-gradient(135deg, #66bb6a, #aed581)",
    avatarShadow: "0 2px 8px rgba(102,187,106,0.3)",
    userMsgBg: "linear-gradient(135deg, #66bb6a, #aed581)",
    userMsgColor: "#fff",
    userMsgShadow: "0 4px 14px rgba(102,187,106,0.3)",
    aiBubbleBg: "#fff",
    aiBubbleColor: "#2d4a2d",
    aiBubbleShadow: "0 2px 10px rgba(0,0,0,0.06)",
    aiBubbleBorder: "1.5px solid rgba(150,210,150,0.25)",
    dotBg: "linear-gradient(135deg, #66bb6a, #aed581)",
    hintBg: "linear-gradient(90deg, #f0f7f0, #f5f0e8)",
    hintColor: "#8aaa8a",
    hintBorder: "rgba(150,210,150,0.2)",
    inputBg: "#f0f7f0",
    inputBorder: "rgba(102,187,106,0.25)",
    inputColor: "#2d4a2d",
    inputPlaceholder: "#9ac49a",
    sendBg: "linear-gradient(135deg, #66bb6a, #aed581)",
    sendShadow: "0 4px 14px rgba(102,187,106,0.35)",
    clearBg: "#f0f7f0",
    clearBorder: "rgba(102,187,106,0.2)",
    clearColor: "#8aaa8a",
    footerColor: "#8aaa8a",
    authorColor: "#388e3c",
    traceHeaderColor: "#388e3c",
    traceBg: "linear-gradient(135deg, #f0f7f0, #e8f5e9)",
    traceCardBg: "#fff",
    traceCardBorder: "#66bb6a",
    traceStepColor: "#388e3c",
    traceDetailColor: "#4a7a4a",
    traceTimeColor: "#9ac49a",
    suggBg: "#e8f5e9",
    suggBorder: "rgba(102,187,106,0.3)",
    suggColor: "#5a8a5a",
    inputAreaBg: "rgba(255,255,255,0.6)",
    inputAreaBorder: "rgba(150,210,150,0.2)",
    scrollThumb: "rgba(102,187,106,0.3)",
    font: "'Palatino Linotype', Georgia, serif",
  },
  midnight: {
    name: "🖤 Midnight",
    pageBackground: "linear-gradient(145deg, #0a0a0f, #111118, #0f0f1a)",
    blob1: "transparent",
    blob2: "transparent",
    cardBg: "rgba(255,255,255,0.04)",
    cardBorder: "rgba(150,150,255,0.12)",
    cardShadow: "0 20px 60px rgba(0,0,0,0.6), 0 0 0 1px rgba(150,150,255,0.08)",
    titleColor: "#e8e8ff",
    subtitleColor: "#7070a0",
    badgeBg: "rgba(150,100,255,0.2)",
    badgeColor: "#c0a0ff",
    pillActive: "linear-gradient(135deg, #9060ff, #c060ff)",
    pillActiveShadow: "0 4px 20px rgba(150,100,255,0.4)",
    pillInactive: "rgba(255,255,255,0.04)",
    pillInactiveColor: "#7070a0",
    avatarBg: "linear-gradient(135deg, #9060ff, #c060ff)",
    avatarShadow: "0 2px 12px rgba(150,100,255,0.4)",
    userMsgBg: "linear-gradient(135deg, #9060ff, #c060ff)",
    userMsgColor: "#fff",
    userMsgShadow: "0 4px 20px rgba(150,100,255,0.3)",
    aiBubbleBg: "rgba(255,255,255,0.05)",
    aiBubbleColor: "#c8c8e8",
    aiBubbleShadow: "none",
    aiBubbleBorder: "1px solid rgba(150,150,255,0.12)",
    dotBg: "linear-gradient(135deg, #9060ff, #c060ff)",
    hintBg: "rgba(150,100,255,0.05)",
    hintColor: "#505070",
    hintBorder: "rgba(150,150,255,0.08)",
    inputBg: "rgba(255,255,255,0.05)",
    inputBorder: "rgba(150,150,255,0.15)",
    inputColor: "#c8c8e8",
    inputPlaceholder: "#404060",
    sendBg: "linear-gradient(135deg, #9060ff, #c060ff)",
    sendShadow: "0 4px 20px rgba(150,100,255,0.35)",
    clearBg: "rgba(255,255,255,0.04)",
    clearBorder: "rgba(150,150,255,0.12)",
    clearColor: "#505070",
    footerColor: "#404060",
    authorColor: "#a080ff",
    traceHeaderColor: "#a080ff",
    traceBg: "rgba(0,0,0,0.4)",
    traceCardBg: "rgba(150,100,255,0.07)",
    traceCardBorder: "#9060ff",
    traceStepColor: "#a080ff",
    traceDetailColor: "#8080b0",
    traceTimeColor: "#404060",
    suggBg: "rgba(150,100,255,0.08)",
    suggBorder: "rgba(150,100,255,0.2)",
    suggColor: "#9070cc",
    inputAreaBg: "rgba(0,0,0,0.2)",
    inputAreaBorder: "rgba(150,150,255,0.08)",
    scrollThumb: "rgba(150,100,255,0.3)",
    font: "'Georgia', serif",
  },
};

const AGENT_TRACE = [];
function logTrace(step, detail) {
  AGENT_TRACE.push({ step, detail, time: new Date().toLocaleTimeString() });
}

const MODES = [
  { id: "chat",      emoji: "💬", label: "Ask Anything" },
  { id: "quiz",      emoji: "🧠", label: "Quiz Me"      },
  { id: "flashcard", emoji: "🃏", label: "Flashcards"   },
  { id: "explain",   emoji: "📖", label: "Explain"      },
  { id: "trace",     emoji: "🔍", label: "Agent Trace"  },
];

const SUGGESTIONS = [
  "Explain photosynthesis 🌿",
  "Quiz me on World War 2 ⚔️",
  "Flashcards for Newton's Laws 🍎",
  "What is machine learning? 🤖",
  "Summarize the water cycle 💧",
];

export default function AIStudyBuddy() {
  const [themeKey, setThemeKey] = useState("pinterest");
  const [mode, setMode]         = useState("chat");
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hi there! 🌸 I'm your AI Study Buddy! Ask me anything — I can explain concepts, quiz you, or make flashcards. What shall we learn today? ✨" }
  ]);
  const [input, setInput]       = useState("");
  const [loading, setLoading]   = useState(false);
  const [traceLog, setTraceLog] = useState([]);
  const [showThemes, setShowThemes] = useState(false);
  const bottomRef = useRef(null);
  const t = THEMES[themeKey];

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const getModePrompt = (text) => {
    if (mode === "quiz")      return `Generate 5 multiple choice quiz questions about: "${text}"`;
    if (mode === "flashcard") return `Create 5 flashcards about: "${text}"`;
    if (mode === "explain")   return `Explain this in very simple beginner-friendly language with a relatable example: "${text}"`;
    return text;
  };

  const sendMessage = async (text) => {
    const userText = (text || input).trim();
    if (!userText || loading) return;
    setInput("");
    setLoading(true);

    const userMsg = { role: "user", content: userText };
    const updated = [...messages, userMsg];
    setMessages(updated);

    logTrace("Input Received", `Mode: ${mode} | "${userText}"`);
    logTrace("Prompt Built", getModePrompt(userText));
    logTrace("API Called", "claude-sonnet-4-20250514");
    setTraceLog([...AGENT_TRACE]);

    try {
      const apiMessages = updated.map((m, i) => ({
        role: m.role,
        content: i === updated.length - 1 && m.role === "user" ? getModePrompt(userText) : m.content,
      }));
      const res  = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: "claude-sonnet-4-20250514",
          max_tokens: 1000,
          system: SYSTEM_PROMPT,
          messages: apiMessages,
        }),
      });
      const data  = await res.json();
      const reply = data.content?.[0]?.text || "Hmm, something went wrong. Try again!";
      logTrace("Response Received", `${reply.length} chars`);
      setTraceLog([...AGENT_TRACE]);
      setMessages(prev => [...prev, { role: "assistant", content: reply }]);
    } catch (e) {
      logTrace("Error", e.message);
      setMessages(prev => [...prev, { role: "assistant", content: "⚠️ Oops! Please try again." }]);
    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    setMessages([{ role: "assistant", content: "Chat cleared! 🌸 What would you like to study next?" }]);
    AGENT_TRACE.length = 0;
    setTraceLog([]);
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: t.pageBackground,
      fontFamily: t.font,
      padding: "28px 16px 40px",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      transition: "background 0.5s ease",
    }}>

      {/* Blobs */}
      {t.blob1 !== "transparent" && <>
        <div style={{ position:"fixed", top:"-80px", right:"-80px", width:"320px", height:"320px", borderRadius:"50%", background:`radial-gradient(circle, ${t.blob1} 0%, transparent 70%)`, opacity:0.5, pointerEvents:"none", transition:"all 0.5s" }} />
        <div style={{ position:"fixed", bottom:"-60px", left:"-60px", width:"260px", height:"260px", borderRadius:"50%", background:`radial-gradient(circle, ${t.blob2} 0%, transparent 70%)`, opacity:0.5, pointerEvents:"none", transition:"all 0.5s" }} />
      </>}

      {/* Header */}
      <div style={{ textAlign:"center", marginBottom:"20px", animation:"fadeDown 0.6s ease" }}>
        <div style={{ fontSize:"52px", marginBottom:"6px" }}>📚</div>
        <h1 style={{ fontSize:"2.4rem", fontWeight:"700", color:t.titleColor, margin:"0 0 6px", letterSpacing:"-0.5px", transition:"color 0.4s" }}>
          AI Study Buddy
        </h1>
        <p style={{ color:t.subtitleColor, fontSize:"0.9rem", margin:"0 0 12px", fontStyle:"italic", transition:"color 0.4s" }}>
          your cozy corner for learning ✨
        </p>
        <span style={{
          background:t.badgeBg, color:t.badgeColor,
          padding:"4px 16px", borderRadius:"20px",
          fontSize:"0.72rem", fontWeight:"600",
          letterSpacing:"0.5px",
          border: themeKey === "galaxy" ? "1px solid #f9c74f" : themeKey === "midnight" ? "1px solid rgba(150,100,255,0.3)" : "none",
        }}>
          🏆 Gradio Build-Small Hackathon 2026
        </span>
      </div>

      {/* Theme Switcher */}
      <div style={{ marginBottom:"16px", position:"relative" }}>
        <button onClick={() => setShowThemes(p => !p)} style={{
          padding:"8px 20px", borderRadius:"30px", border:"none",
          background: t.pillActive, color:"#fff",
          fontWeight:"700", fontSize:"0.82rem",
          cursor:"pointer", fontFamily:"inherit",
          boxShadow: t.pillActiveShadow,
        }}>
          🎨 Theme: {t.name} {showThemes ? "▲" : "▼"}
        </button>
        {showThemes && (
          <div style={{
            position:"absolute", top:"44px", left:"50%", transform:"translateX(-50%)",
            background: themeKey === "galaxy" || themeKey === "midnight" ? "rgba(30,30,50,0.95)" : "#fff",
            borderRadius:"16px", padding:"10px",
            boxShadow:"0 8px 32px rgba(0,0,0,0.2)",
            display:"flex", flexDirection:"column", gap:"6px",
            zIndex:100, minWidth:"180px",
            border:`1px solid ${t.cardBorder}`,
          }}>
            {Object.entries(THEMES).map(([key, th]) => (
              <button key={key} onClick={() => { setThemeKey(key); setShowThemes(false); }} style={{
                padding:"8px 16px", borderRadius:"12px", border:"none",
                background: themeKey === key ? th.pillActive : "transparent",
                color: themeKey === key ? "#fff" : t.subtitleColor,
                fontWeight: themeKey === key ? "700" : "500",
                fontSize:"0.82rem", cursor:"pointer",
                fontFamily:"inherit", textAlign:"left",
                transition:"all 0.2s",
              }}>
                {th.name}
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Mode Pills */}
      <div style={{ display:"flex", gap:"8px", flexWrap:"wrap", justifyContent:"center", marginBottom:"20px", maxWidth:"720px" }}>
        {MODES.map(m => (
          <button key={m.id} onClick={() => setMode(m.id)} style={{
            padding:"8px 18px", borderRadius:"30px", border:"none",
            background: mode === m.id ? t.pillActive : t.pillInactive,
            color: mode === m.id ? "#fff" : t.pillInactiveColor,
            fontWeight: mode === m.id ? "700" : "500",
            fontSize:"0.82rem", cursor:"pointer",
            boxShadow: mode === m.id ? t.pillActiveShadow : "0 2px 8px rgba(0,0,0,0.06)",
            transition:"all 0.2s", fontFamily:"inherit",
          }}>
            {m.emoji} {m.label}
          </button>
        ))}
      </div>

      {/* Main Card */}
      <div style={{
        width:"100%", maxWidth:"720px",
        background:t.cardBg,
        backdropFilter:"blur(16px)",
        borderRadius:"28px",
        border:`1.5px solid ${t.cardBorder}`,
        boxShadow:t.cardShadow,
        overflow:"hidden",
        transition:"all 0.4s ease",
      }}>

        {/* Agent Trace */}
        {mode === "trace" && (
          <div style={{
            padding:"20px", background:t.traceBg,
            borderBottom:`1.5px solid ${t.hintBorder}`,
            maxHeight:"260px", overflowY:"auto",
          }}>
            <h3 style={{ color:t.traceHeaderColor, margin:"0 0 12px", fontSize:"0.95rem", fontWeight:"700" }}>🔍 Agent Trace Log</h3>
            {traceLog.length === 0
              ? <p style={{ color:t.traceTimeColor, fontSize:"0.82rem", fontStyle:"italic" }}>No trace yet — ask a question first!</p>
              : traceLog.map((tr, i) => (
                <div key={i} style={{
                  marginBottom:"10px", padding:"10px 14px",
                  background:t.traceCardBg, borderRadius:"14px",
                  borderLeft:`3px solid ${t.traceCardBorder}`,
                }}>
                  <div style={{ color:t.traceStepColor, fontSize:"0.76rem", fontWeight:"700" }}>Step {i+1}: {tr.step}</div>
                  <div style={{ color:t.traceDetailColor, fontSize:"0.78rem", marginTop:"3px", wordBreak:"break-word" }}>{tr.detail}</div>
                  <div style={{ color:t.traceTimeColor, fontSize:"0.7rem", marginTop:"2px" }}>{tr.time}</div>
                </div>
              ))
            }
          </div>
        )}

        {/* Suggestions */}
        {messages.length <= 1 && mode === "chat" && (
          <div style={{ padding:"16px 20px 0", display:"flex", gap:"8px", flexWrap:"wrap" }}>
            {SUGGESTIONS.map((s, i) => (
              <button key={i} onClick={() => sendMessage(s)} style={{
                padding:"6px 14px", borderRadius:"20px",
                border:`1.5px solid ${t.suggBorder}`,
                background:t.suggBg, color:t.suggColor,
                fontSize:"0.76rem", cursor:"pointer",
                fontFamily:"inherit", transition:"all 0.2s",
              }}>{s}</button>
            ))}
          </div>
        )}

        {/* Messages */}
        <div style={{ height:"400px", overflowY:"auto", padding:"20px", display:"flex", flexDirection:"column", gap:"14px" }}>
          {messages.map((msg, i) => (
            <div key={i} style={{ display:"flex", justifyContent: msg.role === "user" ? "flex-end" : "flex-start", animation:"fadeUp 0.3s ease" }}>
              {msg.role === "assistant" && (
                <div style={{
                  width:"34px", height:"34px", borderRadius:"50%",
                  background:t.avatarBg,
                  display:"flex", alignItems:"center", justifyContent:"center",
                  fontSize:"17px", marginRight:"8px", flexShrink:0, marginTop:"4px",
                  boxSimport { useState, useRef, useEffect } from "react";

const SYSTEM_PROMPT = `You are an AI Study Buddy — a friendly, warm, and encouraging study assistant. Help students learn better.

You can:
1. Explain concepts in simple, easy-to-understand language
2. Generate quiz questions on any topic
3. Create flashcards (Q&A format)
4. Summarize notes or topics
5. Answer study-related questions

Always be warm, encouraging, and supportive. Use emojis occasionally to keep things fun 📚✨

Format quizzes like:
Q1. [Question]
a) option  b) option  c) option  d) option
✅ Answer: [correct]

Format flashcards like:
🃏 Flashcard 1
Front: [concept]
Back: [explanation]`;

const THEMES = {
  pinterest: {
    name: "🌸 Pinterest",
    pageBackground: "linear-gradient(145deg, #fff5f7 0%, #fef9f0 40%, #f0f4ff 100%)",
    blob1: "#ffd6e0",
    blob2: "#d4e8ff",
    cardBg: "rgba(255,255,255,0.82)",
    cardBorder: "rgba(255,200,200,0.3)",
    cardShadow: "0 8px 40px rgba(255,143,171,0.12), 0 2px 8px rgba(0,0,0,0.06)",
    titleColor: "#3d2c2c",
    subtitleColor: "#a07070",
    badgeBg: "linear-gradient(135deg, #ff8fab, #ffb347)",
    badgeColor: "#fff",
    pillActive: "linear-gradient(135deg, #ff8fab, #ffb347)",
    pillActiveShadow: "0 4px 16px rgba(255,143,171,0.4)",
    pillInactive: "rgba(255,255,255,0.8)",
    pillInactiveColor: "#8a6060",
    avatarBg: "linear-gradient(135deg, #ff8fab, #ffb347)",
    avatarShadow: "0 2px 8px rgba(255,143,171,0.35)",
    userMsgBg: "linear-gradient(135deg, #ff8fab, #ffb347)",
    userMsgColor: "#fff",
    userMsgShadow: "0 4px 16px rgba(255,143,171,0.35)",
    aiBubbleBg: "#fff",
    aiBubbleColor: "#4a3030",
    aiBubbleShadow: "0 2px 12px rgba(0,0,0,0.07)",
    aiBubbleBorder: "1.5px solid rgba(255,200,200,0.2)",
    dotBg: "linear-gradient(135deg, #ff8fab, #ffb347)",
    hintBg: "linear-gradient(90deg, #fff5f7, #fef9f0)",
    hintColor: "#c4a0a0",
    hintBorder: "rgba(255,200,200,0.2)",
    inputBg: "#fff5f7",
    inputBorder: "rgba(255,143,171,0.25)",
    inputColor: "#4a3030",
    inputPlaceholder: "#d4a0a0",
    sendBg: "linear-gradient(135deg, #ff8fab, #ffb347)",
    sendShadow: "0 4px 14px rgba(255,143,171,0.4)",
    clearBg: "#fff5f7",
    clearBorder: "rgba(255,143,171,0.2)",
    clearColor: "#c4a0a0",
    footerColor: "#c4a0a0",
    authorColor: "#e8627a",
    traceHeaderColor: "#e8627a",
    traceBg: "linear-gradient(135deg, #fff5f7, #fef9f0)",
    traceCardBg: "#fff",
    traceCardBorder: "#ff8fab",
    traceStepColor: "#e8627a",
    traceDetailColor: "#7a5c5c",
    traceTimeColor: "#c4a0a0",
    suggBg: "#fff5f7",
    suggBorder: "rgba(255,143,171,0.3)",
    suggColor: "#c07080",
    inputAreaBg: "rgba(255,255,255,0.6)",
    inputAreaBorder: "rgba(255,200,200,0.2)",
    scrollThumb: "rgba(255,143,171,0.3)",
    font: "'Palatino Linotype', Georgia, serif",
  },
  galaxy: {
    name: "🌌 Galaxy",
    pageBackground: "linear-gradient(135deg, #0f0c29, #302b63, #24243e)",
    blob1: "transparent",
    blob2: "transparent",
    cardBg: "rgba(255,255,255,0.05)",
    cardBorder: "rgba(255,255,255,0.1)",
    cardShadow: "0 25px 60px rgba(0,0,0,0.4)",
    titleColor: "#fff",
    subtitleColor: "#a0aec0",
    badgeBg: "rgba(249,199,79,0.15)",
    badgeColor: "#f9c74f",
    pillActive: "linear-gradient(135deg, #f9c74f, #f3722c)",
    pillActiveShadow: "0 4px 16px rgba(249,199,79,0.3)",
    pillInactive: "rgba(255,255,255,0.07)",
    pillInactiveColor: "#a0aec0",
    avatarBg: "linear-gradient(135deg, #f9c74f, #f3722c)",
    avatarShadow: "0 2px 8px rgba(249,199,79,0.3)",
    userMsgBg: "linear-gradient(135deg, #f9c74f, #f8961e)",
    userMsgColor: "#1a1a2e",
    userMsgShadow: "none",
    aiBubbleBg: "rgba(255,255,255,0.08)",
    aiBubbleColor: "#e2e8f0",
    aiBubbleShadow: "none",
    aiBubbleBorder: "1px solid rgba(255,255,255,0.1)",
    dotBg: "#f9c74f",
    hintBg: "rgba(249,199,79,0.05)",
    hintColor: "#718096",
    hintBorder: "rgba(255,255,255,0.06)",
    inputBg: "rgba(255,255,255,0.08)",
    inputBorder: "rgba(255,255,255,0.15)",
    inputColor: "#e2e8f0",
    inputPlaceholder: "#4a5568",
    sendBg: "linear-gradient(135deg, #f9c74f, #f3722c)",
    sendShadow: "none",
    clearBg: "rgba(255,255,255,0.05)",
    clearBorder: "rgba(255,255,255,0.15)",
    clearColor: "#718096",
    footerColor: "#4a5568",
    authorColor: "#f9c74f",
    traceHeaderColor: "#f9c74f",
    traceBg: "rgba(0,0,0,0.3)",
    traceCardBg: "rgba(249,199,79,0.08)",
    traceCardBorder: "#f9c74f",
    traceStepColor: "#f9c74f",
    traceDetailColor: "#cbd5e0",
    traceTimeColor: "#4a5568",
    suggBg: "rgba(249,199,79,0.08)",
    suggBorder: "rgba(249,199,79,0.2)",
    suggColor: "#f9c74f",
    inputAreaBg: "rgba(0,0,0,0.15)",
    inputAreaBorder: "rgba(255,255,255,0.08)",
    scrollThumb: "rgba(249,199,79,0.3)",
    font: "'Georgia', serif",
  },
  matcha: {
    name: "🍵 Matcha",
    pageBackground: "linear-gradient(145deg, #f0f7f0 0%, #e8f5e9 50%, #f5f0e8 100%)",
    blob1: "#c8e6c9",
    blob2: "#dcedc8",
    cardBg: "rgba(255,255,255,0.85)",
    cardBorder: "rgba(150,210,150,0.3)",
    cardShadow: "0 8px 40px rgba(100,180,100,0.1), 0 2px 8px rgba(0,0,0,0.05)",
    titleColor: "#2d4a2d",
    subtitleColor: "#6a9a6a",
    badgeBg: "linear-gradient(135deg, #81c784, #aed581)",
    badgeColor: "#fff",
    pillActive: "linear-gradient(135deg, #66bb6a, #aed581)",
    pillActiveShadow: "0 4px 16px rgba(102,187,106,0.35)",
    pillInactive: "rgba(255,255,255,0.85)",
    pillInactiveColor: "#5a8a5a",
    avatarBg: "linear-gradient(135deg, #66bb6a, #aed581)",
    avatarShadow: "0 2px 8px rgba(102,187,106,0.3)",
    userMsgBg: "linear-gradient(135deg, #66bb6a, #aed581)",
    userMsgColor: "#fff",
    userMsgShadow: "0 4px 14px rgba(102,187,106,0.3)",
    aiBubbleBg: "#fff",
    aiBubbleColor: "#2d4a2d",
    aiBubbleShadow: "0 2px 10px rgba(0,0,0,0.06)",
    aiBubbleBorder: "1.5px solid rgba(150,210,150,0.25)",
    dotBg: "linear-gradient(135deg, #66bb6a, #aed581)",
    hintBg: "linear-gradient(90deg, #f0f7f0, #f5f0e8)",
    hintColor: "#8aaa8a",
    hintBorder: "rgba(150,210,150,0.2)",
    inputBg: "#f0f7f0",
    inputBorder: "rgba(102,187,106,0.25)",
    inputColor: "#2d4a2d",
    inputPlaceholder: "#9ac49a",
    sendBg: "linear-gradient(135deg, #66bb6a, #aed581)",
    sendShadow: "0 4px 14px rgba(102,187,106,0.35)",
    clearBg: "#f0f7f0",
    clearBorder: "rgba(102,187,106,0.2)",
    clearColor: "#8aaa8a",
    footerColor: "#8aaa8a",
    authorColor: "#388e3c",
    traceHeaderColor: "#388e3c",
    traceBg: "linear-gradient(135deg, #f0f7f0, #e8f5e9)",
    traceCardBg: "#fff",
    traceCardBorder: "#66bb6a",
    traceStepColor: "#388e3c",
    traceDetailColor: "#4a7a4a",
    traceTimeColor: "#9ac49a",
    suggBg: "#e8f5e9",
    suggBorder: "rgba(102,187,106,0.3)",
    suggColor: "#5a8a5a",
    inputAreaBg: "rgba(255,255,255,0.6)",
    inputAreaBorder: "rgba(150,210,150,0.2)",
    scrollThumb: "rgba(102,187,106,0.3)",
    font: "'Palatino Linotype', Georgia, serif",
  },
  midnight: {
    name: "🖤 Midnight",
    pageBackground: "linear-gradient(145deg, #0a0a0f, #111118, #0f0f1a)",
    blob1: "transparent",
    blob2: "transparent",
    cardBg: "rgba(255,255,255,0.04)",
    cardBorder: "rgba(150,150,255,0.12)",
    cardShadow: "0 20px 60px rgba(0,0,0,0.6), 0 0 0 1px rgba(150,150,255,0.08)",
    titleColor: "#e8e8ff",
    subtitleColor: "#7070a0",
    badgeBg: "rgba(150,100,255,0.2)",
    badgeColor: "#c0a0ff",
    pillActive: "linear-gradient(135deg, #9060ff, #c060ff)",
    pillActiveShadow: "0 4px 20px rgba(150,100,255,0.4)",
    pillInactive: "rgba(255,255,255,0.04)",
    pillInactiveColor: "#7070a0",
    avatarBg: "linear-gradient(135deg, #9060ff, #c060ff)",
    avatarShadow: "0 2px 12px rgba(150,100,255,0.4)",
    userMsgBg: "linear-gradient(135deg, #9060ff, #c060ff)",
    userMsgColor: "#fff",
    userMsgShadow: "0 4px 20px rgba(150,100,255,0.3)",
    aiBubbleBg: "rgba(255,255,255,0.05)",
    aiBubbleColor: "#c8c8e8",
    aiBubbleShadow: "none",
    aiBubbleBorder: "1px solid rgba(150,150,255,0.12)",
    dotBg: "linear-gradient(135deg, #9060ff, #c060ff)",
    hintBg: "rgba(150,100,255,0.05)",
    hintColor: "#505070",
    hintBorder: "rgba(150,150,255,0.08)",
    inputBg: "rgba(255,255,255,0.05)",
    inputBorder: "rgba(150,150,255,0.15)",
    inputColor: "#c8c8e8",
    inputPlaceholder: "#404060",
    sendBg: "linear-gradient(135deg, #9060ff, #c060ff)",
    sendShadow: "0 4px 20px rgba(150,100,255,0.35)",
    clearBg: "rgba(255,255,255,0.04)",
    clearBorder: "rgba(150,150,255,0.12)",
    clearColor: "#505070",
    footerColor: "#404060",
    authorColor: "#a080ff",
    traceHeaderColor: "#a080ff",
    traceBg: "rgba(0,0,0,0.4)",
    traceCardBg: "rgba(150,100,255,0.07)",
    traceCardBorder: "#9060ff",
    traceStepColor: "#a080ff",
    traceDetailColor: "#8080b0",
    traceTimeColor: "#404060",
    suggBg: "rgba(150,100,255,0.08)",
    suggBorder: "rgba(150,100,255,0.2)",
    suggColor: "#9070cc",
    inputAreaBg: "rgba(0,0,0,0.2)",
    inputAreaBorder: "rgba(150,150,255,0.08)",
    scrollThumb: "rgba(150,100,255,0.3)",
    font: "'Georgia', serif",
  },
};

const AGENT_TRACE = [];
function logTrace(step, detail) {
  AGENT_TRACE.push({ step, detail, time: new Date().toLocaleTimeString() });
}

const MODES = [
  { id: "chat",      emoji: "💬", label: "Ask Anything" },
  { id: "quiz",      emoji: "🧠", label: "Quiz Me"      },
  { id: "flashcard", emoji: "🃏", label: "Flashcards"   },
  { id: "explain",   emoji: "📖", label: "Explain"      },
  { id: "trace",     emoji: "🔍", label: "Agent Trace"  },
];

const SUGGESTIONS = [
  "Explain photosynthesis 🌿",
  "Quiz me on World War 2 ⚔️",
  "Flashcards for Newton's Laws 🍎",
  "What is machine learning? 🤖",
  "Summarize the water cycle 💧",
];

export default function AIStudyBuddy() {
  const [themeKey, setThemeKey] = useState("pinterest");
  const [mode, setMode]         = useState("chat");
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hi there! 🌸 I'm your AI Study Buddy! Ask me anything — I can explain concepts, quiz you, or make flashcards. What shall we learn today? ✨" }
  ]);
  const [input, setInput]       = useState("");
  const [loading, setLoading]   = useState(false);
  const [traceLog, setTraceLog] = useState([]);
  const [showThemes, setShowThemes] = useState(false);
  const bottomRef = useRef(null);
  const t = THEMES[themeKey];

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const getModePrompt = (text) => {
    if (mode === "quiz")      return `Generate 5 multiple choice quiz questions about: "${text}"`;
    if (mode === "flashcard") return `Create 5 flashcards about: "${text}"`;
    if (mode === "explain")   return `Explain this in very simple beginner-friendly language with a relatable example: "${text}"`;
    return text;
  };

  const sendMessage = async (text) => {
    const userText = (text || input).trim();
    if (!userText || loading) return;
    setInput("");
    setLoading(true);

    const userMsg = { role: "user", content: userText };
    const updated = [...messages, userMsg];
    setMessages(updated);

    logTrace("Input Received", `Mode: ${mode} | "${userText}"`);
    logTrace("Prompt Built", getModePrompt(userText));
    logTrace("API Called", "claude-sonnet-4-20250514");
    setTraceLog([...AGENT_TRACE]);

    try {
      const apiMessages = updated.map((m, i) => ({
        role: m.role,
        content: i === updated.length - 1 && m.role === "user" ? getModePrompt(userText) : m.content,
      }));
      const res  = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: "claude-sonnet-4-20250514",
          max_tokens: 1000,
          system: SYSTEM_PROMPT,
          messages: apiMessages,
        }),
      });
      const data  = await res.json();
      const reply = data.content?.[0]?.text || "Hmm, something went wrong. Try again!";
      logTrace("Response Received", `${reply.length} chars`);
      setTraceLog([...AGENT_TRACE]);
      setMessages(prev => [...prev, { role: "assistant", content: reply }]);
    } catch (e) {
      logTrace("Error", e.message);
      setMessages(prev => [...prev, { role: "assistant", content: "⚠️ Oops! Please try again." }]);
    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    setMessages([{ role: "assistant", content: "Chat cleared! 🌸 What would you like to study next?" }]);
    AGENT_TRACE.length = 0;
    setTraceLog([]);
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: t.pageBackground,
      fontFamily: t.font,
      padding: "28px 16px 40px",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      transition: "background 0.5s ease",
    }}>

      {/* Blobs */}
      {t.blob1 !== "transparent" && <>
        <div style={{ position:"fixed", top:"-80px", right:"-80px", width:"320px", height:"320px", borderRadius:"50%", background:`radial-gradient(circle, ${t.blob1} 0%, transparent 70%)`, opacity:0.5, pointerEvents:"none", transition:"all 0.5s" }} />
        <div style={{ position:"fixed", bottom:"-60px", left:"-60px", width:"260px", height:"260px", borderRadius:"50%", background:`radial-gradient(circle, ${t.blob2} 0%, transparent 70%)`, opacity:0.5, pointerEvents:"none", transition:"all 0.5s" }} />
      </>}

      {/* Header */}
      <div style={{ textAlign:"center", marginBottom:"20px", animation:"fadeDown 0.6s ease" }}>
        <div style={{ fontSize:"52px", marginBottom:"6px" }}>📚</div>
        <h1 style={{ fontSize:"2.4rem", fontWeight:"700", color:t.titleColor, margin:"0 0 6px", letterSpacing:"-0.5px", transition:"color 0.4s" }}>
          AI Study Buddy
        </h1>
        <p style={{ color:t.subtitleColor, fontSize:"0.9rem", margin:"0 0 12px", fontStyle:"italic", transition:"color 0.4s" }}>
          your cozy corner for learning ✨
        </p>
        <span style={{
          background:t.badgeBg, color:t.badgeColor,
          padding:"4px 16px", borderRadius:"20px",
          fontSize:"0.72rem", fontWeight:"600",
          letterSpacing:"0.5px",
          border: themeKey === "galaxy" ? "1px solid #f9c74f" : themeKey === "midnight" ? "1px solid rgba(150,100,255,0.3)" : "none",
        }}>
          🏆 Gradio Build-Small Hackathon 2026
        </span>
      </div>

      {/* Theme Switcher */}
      <div style={{ marginBottom:"16px", position:"relative" }}>
        <button onClick={() => setShowThemes(p => !p)} style={{
          padding:"8px 20px", borderRadius:"30px", border:"none",
          background: t.pillActive, color:"#fff",
          fontWeight:"700", fontSize:"0.82rem",
          cursor:"pointer", fontFamily:"inherit",
          boxShadow: t.pillActiveShadow,
        }}>
          🎨 Theme: {t.name} {showThemes ? "▲" : "▼"}
        </button>
        {showThemes && (
          <div style={{
            position:"absolute", top:"44px", left:"50%", transform:"translateX(-50%)",
            background: themeKey === "galaxy" || themeKey === "midnight" ? "rgba(30,30,50,0.95)" : "#fff",
            borderRadius:"16px", padding:"10px",
            boxShadow:"0 8px 32px rgba(0,0,0,0.2)",
            display:"flex", flexDirection:"column", gap:"6px",
            zIndex:100, minWidth:"180px",
            border:`1px solid ${t.cardBorder}`,
          }}>
            {Object.entries(THEMES).map(([key, th]) => (
              <button key={key} onClick={() => { setThemeKey(key); setShowThemes(false); }} style={{
                padding:"8px 16px", borderRadius:"12px", border:"none",
                background: themeKey === key ? th.pillActive : "transparent",
                color: themeKey === key ? "#fff" : t.subtitleColor,
                fontWeight: themeKey === key ? "700" : "500",
                fontSize:"0.82rem", cursor:"pointer",
                fontFamily:"inherit", textAlign:"left",
                transition:"all 0.2s",
              }}>
                {th.name}
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Mode Pills */}
      <div style={{ display:"flex", gap:"8px", flexWrap:"wrap", justifyContent:"center", marginBottom:"20px", maxWidth:"720px" }}>
        {MODES.map(m => (
          <button key={m.id} onClick={() => setMode(m.id)} style={{
            padding:"8px 18px", borderRadius:"30px", border:"none",
            background: mode === m.id ? t.pillActive : t.pillInactive,
            color: mode === m.id ? "#fff" : t.pillInactiveColor,
            fontWeight: mode === m.id ? "700" : "500",
            fontSize:"0.82rem", cursor:"pointer",
            boxShadow: mode === m.id ? t.pillActiveShadow : "0 2px 8px rgba(0,0,0,0.06)",
            transition:"all 0.2s", fontFamily:"inherit",
          }}>
            {m.emoji} {m.label}
          </button>
        ))}
      </div>

      {/* Main Card */}
      <div style={{
        width:"100%", maxWidth:"720px",
        background:t.cardBg,
        backdropFilter:"blur(16px)",
        borderRadius:"28px",
        border:`1.5px solid ${t.cardBorder}`,
        boxShadow:t.cardShadow,
        overflow:"hidden",
        transition:"all 0.4s ease",
      }}>

        {/* Agent Trace */}
        {mode === "trace" && (
          <div style={{
            padding:"20px", background:t.traceBg,
            borderBottom:`1.5px solid ${t.hintBorder}`,
            maxHeight:"260px", overflowY:"auto",
          }}>
            <h3 style={{ color:t.traceHeaderColor, margin:"0 0 12px", fontSize:"0.95rem", fontWeight:"700" }}>🔍 Agent Trace Log</h3>
            {traceLog.length === 0
              ? <p style={{ color:t.traceTimeColor, fontSize:"0.82rem", fontStyle:"italic" }}>No trace yet — ask a question first!</p>
              : traceLog.map((tr, i) => (
                <div key={i} style={{
                  marginBottom:"10px", padding:"10px 14px",
                  background:t.traceCardBg, borderRadius:"14px",
                  borderLeft:`3px solid ${t.traceCardBorder}`,
                }}>
                  <div style={{ color:t.traceStepColor, fontSize:"0.76rem", fontWeight:"700" }}>Step {i+1}: {tr.step}</div>
                  <div style={{ color:t.traceDetailColor, fontSize:"0.78rem", marginTop:"3px", wordBreak:"break-word" }}>{tr.detail}</div>
                  <div style={{ color:t.traceTimeColor, fontSize:"0.7rem", marginTop:"2px" }}>{tr.time}</div>
                </div>
              ))
            }
          </div>
        )}

        {/* Suggestions */}
        {messages.length <= 1 && mode === "chat" && (
          <div style={{ padding:"16px 20px 0", display:"flex", gap:"8px", flexWrap:"wrap" }}>
            {SUGGESTIONS.map((s, i) => (
              <button key={i} onClick={() => sendMessage(s)} style={{
                padding:"6px 14px", borderRadius:"20px",
                border:`1.5px solid ${t.suggBorder}`,
                background:t.suggBg, color:t.suggColor,
                fontSize:"0.76rem", cursor:"pointer",
                fontFamily:"inherit", transition:"all 0.2s",
              }}>{s}</button>
            ))}
          </div>
        )}

        {/* Messages */}
        <div style={{ height:"400px", overflowY:"auto", padding:"20px", display:"flex", flexDirection:"column", gap:"14px" }}>
          {messages.map((msg, i) => (
            <div key={i} style={{ display:"flex", justifyContent: msg.role === "user" ? "flex-end" : "flex-start", animation:"fadeUp 0.3s ease" }}>
              {msg.role === "assistant" && (
                <div style={{
                  width:"34px", height:"34px", borderRadius:"50%",
                  background:t.avatarBg,
                  display:"flex", alignItems:"center", justifyContent:"center",
                  fontSize:"17px", marginRight:"8px", flexShrink:0, marginTop:"4px",
                  boxS