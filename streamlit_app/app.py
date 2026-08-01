"""
Rule-Based AI Chatbot — Streamlit Web Interface
Author: Nida Sheraz
"""

import streamlit as st
import sys
import os
from PIL import Image, ImageDraw

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from chatbot import get_response, sanitize_input, KNOWLEDGE_BASE, EXIT_COMMANDS


# ---------- CUSTOM FAVICON (replaces default Streamlit logo in browser tab) ----------
@st.cache_resource
def get_favicon():
    img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse((2, 2, 62, 62), outline=(168, 121, 255, 255), width=4, fill=(20, 16, 32, 255))
    draw.ellipse((18, 24, 28, 34), fill=(192, 132, 252, 255))
    draw.ellipse((36, 24, 46, 34), fill=(192, 132, 252, 255))
    draw.arc((16, 28, 48, 50), start=20, end=160, fill=(233, 213, 255, 255), width=3)
    return img


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Rule-Based AI Chatbot",
    page_icon=get_favicon(),
    layout="centered",
    initial_sidebar_state="expanded",
)


# ---------- LOGOS (inline SVG, single line) ----------
BOT_LOGO = '<svg width="34" height="34" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="g1" x1="0" y1="0" x2="40" y2="40" gradientUnits="userSpaceOnUse"><stop offset="0%" stop-color="#a855f7"/><stop offset="100%" stop-color="#4c1d95"/></linearGradient></defs><circle cx="20" cy="20" r="19" stroke="url(#g1)" stroke-width="1.5" fill="rgba(168,121,255,0.12)"/><circle cx="14" cy="17" r="2.2" fill="#c084fc"/><circle cx="26" cy="17" r="2.2" fill="#c084fc"/><path d="M13 25c2 2.5 4.5 3.5 7 3.5s5-1 7-3.5" stroke="#e9d5ff" stroke-width="2" stroke-linecap="round" fill="none"/></svg>'

USER_LOGO = '<svg width="34" height="34" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="20" r="19" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/><circle cx="20" cy="16" r="6" fill="#cbd5e1"/><path d="M8 32c2-6 7-9 12-9s10 3 12 9" fill="#cbd5e1"/></svg>'


# ---------- SESSION STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Hello. I am a rule-based chatbot. Ask me something, or type 'help' to see what I can respond to."}
    ]
if "pending_input" not in st.session_state:
    st.session_state.pending_input = None


# ---------- FIXED PREMIUM DARK THEME ----------
BG = "#0a0a0f"
SURFACE = "rgba(255,255,255,0.04)"
BORDER = "rgba(255,255,255,0.08)"
TEXT = "#e6e6f0"
SUBTEXT = "#9d8bb5"
BOT_BUBBLE = "rgba(255,255,255,0.05)"
USER_BUBBLE = "linear-gradient(135deg, #7c3aed, #a855f7)"
USER_TEXT = "#ffffff"


# ---------- CSS ----------
css = """
<style>
.stApp {
    background: BG;
    color: TEXT;
}

header[data-testid="stHeader"] {
    background: BG;
}

[data-testid="stBottom"] {
    background: BG;
}
[data-testid="stBottom"] > div {
    background: BG;
}
[data-testid="stBottomBlockContainer"] {
    background: BG;
}
[data-testid="stChatInput"] {
    background: BG;
}
[data-testid="stChatInput"] textarea {
    background: SURFACE;
    color: TEXT;
}

[data-testid="stSidebar"] {
    background: SURFACE;
    border-right: 1px solid BORDER;
}
[data-testid="stSidebar"] * {
    color: TEXT;
}
[data-testid="stSidebar"] hr {
    border-color: BORDER;
}
[data-testid="stSidebar"] button {
    background: SURFACE;
    color: TEXT;
    border: 1px solid BORDER;
}

.app-header {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 4px 0 20px 0;
    border-bottom: 1px solid BORDER;
    margin-bottom: 24px;
}
.app-header h1 {
    font-size: 19px;
    font-weight: 700;
    margin: 0;
    color: TEXT;
}
.app-header p {
    font-size: 12.5px;
    color: SUBTEXT;
    margin: 0;
}
.msg-row {
    display: flex;
    gap: 10px;
    margin-bottom: 18px;
    align-items: flex-start;
}
.msg-row.user {
    flex-direction: row-reverse;
}
.bubble {
    max-width: 78%;
    padding: 12px 16px;
    border-radius: 14px;
    font-size: 14.5px;
    line-height: 1.55;
    border: 1px solid BORDER;
}
.bubble.bot {
    background: BOTBUBBLE;
    color: TEXT;
}
.bubble.user {
    background: USERBUBBLE;
    color: USERTEXT;
    border: none;
}
.purpose-box {
    background: SURFACE;
    border: 1px solid BORDER;
    border-radius: 14px;
    padding: 16px 18px;
    margin-bottom: 22px;
    font-size: 13px;
    color: SUBTEXT;
    line-height: 1.6;
}
.purpose-box b {
    color: TEXT;
}
.suggestions-label {
    font-size: 12px;
    color: SUBTEXT;
    margin-bottom: 8px;
    letter-spacing: 0.3px;
    text-transform: uppercase;
}
div[data-testid="stHorizontalBlock"] button {
    background: SURFACE;
    color: TEXT;
    border: 1px solid BORDER;
    border-radius: 10px;
    font-size: 13px;
    padding: 6px 10px;
}
div[data-testid="stHorizontalBlock"] button:hover {
    border-color: #a855f7;
    color: #c084fc;
}
</style>
"""

css = (css
       .replace("BG", BG)
       .replace("SURFACE", SURFACE)
       .replace("BORDER", BORDER)
       .replace("SUBTEXT", SUBTEXT)
       .replace("BOTBUBBLE", BOT_BUBBLE)
       .replace("USERBUBBLE", USER_BUBBLE)
       .replace("USERTEXT", USER_TEXT)
       .replace("TEXT", TEXT))

st.markdown(css, unsafe_allow_html=True)


# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("### About this project")
    st.markdown(
        "A deterministic, rule-based chatbot built as Project 1 of an AI "
        "engineering training track. It demonstrates control flow, intent "
        "matching, and dictionary-based response lookup. The architectural "
        "foundation that precedes probabilistic, model-driven AI systems."
    )
    st.markdown("---")
    st.markdown("### What this bot understands")
    st.markdown(
        "This is a rule-based system. It only responds to exact phrases "
        "listed below (capitalization does not matter, extra spaces are ignored)."
    )
    supported = ", ".join(f"'{k}'" for k in KNOWLEDGE_BASE.keys())
    st.markdown(supported)
    st.markdown("---")
    st.markdown("**Author:** Nida Sheraz")

    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = [
            {"role": "bot", "text": "Hello. I am a rule-based chatbot. Ask me something, or type 'help' to see what I can respond to."}
        ]
        st.rerun()


# ---------- HEADER ----------
header_html = f'<div class="app-header">{BOT_LOGO}<div><h1>Rule-Based AI Chatbot</h1><p>Deterministic response engine &middot; v1.0</p></div></div>'
st.markdown(header_html, unsafe_allow_html=True)


# ---------- PURPOSE SECTION ----------
purpose_html = (
    '<div class="purpose-box"><b>Purpose:</b> This project demonstrates the '
    'foundational logic layer behind conversational AI systems, before machine '
    'learning enters the picture. Every response here is explicitly defined, '
    'traceable, and predictable, illustrating the control-flow principles that '
    'underpin more advanced, generative chatbot architectures.</div>'
)
st.markdown(purpose_html, unsafe_allow_html=True)


# ---------- SUGGESTED PROMPTS ----------
st.markdown('<div class="suggestions-label">Try asking</div>', unsafe_allow_html=True)

suggestions = ["hello", "what can you do", "who made you", "help"]
cols = st.columns(len(suggestions))
for col, phrase in zip(cols, suggestions):
    with col:
        if st.button(phrase, key=f"sugg_{phrase}", use_container_width=True):
            st.session_state.pending_input = phrase


# ---------- CHAT HISTORY ----------
for msg in st.session_state.messages:
    role_class = "user" if msg["role"] == "user" else "bot"
    logo = USER_LOGO if msg["role"] == "user" else BOT_LOGO
    row_html = f'<div class="msg-row {role_class}">{logo}<div class="bubble {role_class}">{msg["text"]}</div></div>'
    st.markdown(row_html, unsafe_allow_html=True)


# ---------- INPUT ----------
def handle_message(text):
    st.session_state.messages.append({"role": "user", "text": text})
    clean = sanitize_input(text)
    if clean in EXIT_COMMANDS:
        reply = KNOWLEDGE_BASE.get("bye", "Goodbye!")
    else:
        reply = get_response(clean, KNOWLEDGE_BASE)
    st.session_state.messages.append({"role": "bot", "text": reply})


typed_input = st.chat_input("Message the chatbot...")

if st.session_state.pending_input:
    handle_message(st.session_state.pending_input)
    st.session_state.pending_input = None
    st.rerun()
elif typed_input:
    handle_message(typed_input)
    st.rerun()