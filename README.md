# Rule-Based AI Chatbot

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A deterministic, rule-based chatbot demonstrating control flow, intent matching, and dictionary-based (O(1)) response lookup. It represents the foundational logic layer behind conversational AI systems, built prior to introducing machine learning. Built as Project 1 of an AI Engineering training track.

**Live Demo:** [Open the live app](https://rule-based-ai-chatbot-m7vwecf932hsj63ah7hxyf.streamlit.app/)

![Chatbot UI](assets/screenshots/chatbot-ui.png)

## Purpose

Every response in this system is explicitly defined, traceable, and predictable, following a deterministic "white box" architecture. This project establishes the control-flow foundation that underpins more advanced, generative chatbot systems.

## Features

- Continuous conversation loop with graceful exit handling
- Case and whitespace-insensitive input sanitization
- Dictionary-based intent matching (O(1) lookup)
- Fallback response for unrecognized input
- Clickable suggestion prompts for quick discovery of supported commands
- Two implementations: command-line (Python) and web interface (Streamlit)
- Custom-branded, premium dark UI with a hand-drawn favicon

## Tech Stack

- Python 3.11
- Streamlit (web interface)
- Pillow (dynamic favicon generation)

## Project Structure

```
rule-based-ai-chatbot/
├── chatbot.py              Core CLI chatbot logic
├── test_chatbot.py         Unit tests
├── requirements.txt
├── streamlit_app/
│   └── app.py               Web interface
├── assets/
│   └── screenshots/
├── README.md
├── LICENSE
└── .gitignore
```

## Run Locally

### CLI version
```bash
python chatbot.py
```

### Web version
```bash
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

## Testing

```bash
python -m unittest test_chatbot.py -v
```

## Roadmap

- [x] CLI version
- [x] Unit tests
- [x] Web interface (Streamlit)
- [x] Deployment (Streamlit Community Cloud)

## Author

Nida Sheraz