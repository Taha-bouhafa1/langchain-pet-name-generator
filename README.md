# LangChain Pet Name Generator

A simple and fun app that generates cool pet names using Large Language Models powered by LangChain and OpenAI. The app takes your pet type and color as inputs and suggests creative names via a Streamlit interface.

---

## Features

- Generate creative pet names based on the type of pet and its color
- Uses OpenAI’s language models through LangChain for natural language generation
- Interactive UI built with Streamlit for easy user input and instant results
- Lightweight and easy to run locally with minimal dependencies

---

## Tech Stack

- Python 3.8+
- LangChain (langchain-community)
- OpenAI API
- Streamlit for UI
- python-dotenv for environment variables management

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (get yours from https://platform.openai.com/account/api-keys)

### Installation and Setup

```bash
git clone https://github.com/YourUsername/langchain-pet-name-generator.git
cd langchain-pet-name-generator
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
echo "OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx" > .env
```
---
## Author

Taha Bouhafa
