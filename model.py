import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langfuse.langchain import CallbackHandler

load_dotenv()

langfuse_handler = CallbackHandler()

def get_model():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found")

    llm = ChatGroq(
        api_key=api_key,
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=100
    )

    return llm, langfuse_handler