from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

def get_embeddings():
    return OpenAIEmbeddings()
# This function initializes and returns OpenAI embeddings.
# It uses the OpenAIEmbeddings class from the langchain_openai module.
