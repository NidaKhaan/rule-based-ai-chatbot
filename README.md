# Rule-Based AI Chatbot

A deterministic, rule-based chatbot built in Python — Project 1 of an AI Engineering training track. Demonstrates control flow, intent matching, and dictionary-based (O(1)) response lookup as a foundation before generative/ML-based systems.

## Features
- Continuous conversation loop
- Case/whitespace-insensitive input sanitization
- Dictionary-based intent matching (5+ intents)
- Fallback response for unrecognized input
- Clean exit command

## Testing
```bash
python -m unittest test_chatbot.py -v
```

## Project Structure
```
rule-based-ai-chatbot/
├── chatbot.py
├── test_chatbot.py
├── README.md
├── LICENSE
└── .gitignore
```

## Tech Stack
Python 3.11

## Run Locally
```bash
python chatbot.py
```

## Roadmap
- [ ] CLI version (v1)
- [ ] Web app version (Flask/Streamlit)
- [ ] Deployment

## Author
Nida Sheraz