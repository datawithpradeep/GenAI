# GenAI

Hands-on projects exploring LLMs, embeddings, and chatbots using Hugging Face, Groq, and Google Gemini.

## Project Structure

- ChatBot/ : chatbots using Groq API and Hugging Face models (local and API based)
- Embedding/ : text embeddings and document similarity using Hugging Face and Gemini
- LLM/ : basic LLM usage, plus a Streamlit UI version

## Setup

1. Clone the repo
git clone https://github.com/datawithpradeep/GenAI.git
cd GenAI


2. Create a virtual environment and install dependencies
pip install -r requirements.txt


3. Create a .env file in the root folder and add your keys
GROQ_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
HF_TOKEN=your_key_here


## Run

python ChatBot/chatmodel_groq.py
streamlit run LLM/model_with_ui.py


## Notes

- Never commit your .env file.
- Local Hugging Face models run best with a GPU (see ChatBot/gpu_config.py).
