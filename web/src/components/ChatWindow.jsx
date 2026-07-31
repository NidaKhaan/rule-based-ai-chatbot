import { useState, useRef, useEffect } from "react";
import MessageBubble from "./MessageBubble";
import { sanitizeInput, getResponse, isExitCommand, KNOWLEDGE_BASE } from "../logic/chatbot";

export default function ChatWindow() {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Hi! I'm a rule-based chatbot. Type 'help' to see what I can do." },
  ]);
  const [input, setInput] = useState("");
  const scrollRef = useRef(null);

  useEffect(() => {
    scrollRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  function handleSend() {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    const clean = sanitizeInput(input);

    let botText;
    if (isExitCommand(clean)) {
      botText = KNOWLEDGE_BASE["bye"];
    } else {
      botText = getResponse(clean);
    }

    const botMessage = { sender: "bot", text: botText };

    setMessages((prev) => [...prev, userMessage, botMessage]);
    setInput("");
  }

  function handleKeyDown(e) {
    if (e.key === "Enter") handleSend();
  }

  return (
    <div className="chat-window">
      <div className="chat-header">Rule-Based AI Chatbot</div>

      <div className="chat-body">
        {messages.map((msg, idx) => (
          <MessageBubble key={idx} sender={msg.sender} text={msg.text} />
        ))}
        <div ref={scrollRef} />
      </div>

      <div className="chat-input-row">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type a message..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}