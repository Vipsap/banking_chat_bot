from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

VECTOR_DB_PATH = "vectorstore/banking_faiss"

def load_agent():
    vectordb = FAISS.load_local(
        VECTOR_DB_PATH,
        OpenAIEmbeddings(),
        allow_dangerous_deserialization=True  # ✅ Must be True
    )
    retriever = vectordb.as_retriever()
    return RetrievalQA.from_chain_type(
        llm=OpenAI(),
        retriever=retriever,
        return_source_documents=True
    )
# This function loads the banking agent using FAISS vector store and OpenAI embeddings.
# It initializes the vector store from the local path and creates a retrieval chain using OpenAI as