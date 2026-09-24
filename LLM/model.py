import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Streamlit configuration
st.set_page_config(
    page_title="LangChain GROQ App",
    page_icon="🤖"
)

st.title("🤖 LangChain GROQ Chatbot")

# User input
question = st.text_input("Ask your question:")

if question:

    # LLM
    llm = ChatGroq(
        model="openai/gpt-oss-20b"
    )

    # Get response
    result = llm.invoke(question)

    # Display response
    st.subheader("Answer:")
    st.write(result.content)