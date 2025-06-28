from langchain_community.vectorstores import FAISS
from utils.embedder import get_embeddings
import math

VECTOR_DB_PATH = "vectorstore/banking_faiss"

def batch_documents(documents, batch_size=50):
    for i in range(0, len(documents), batch_size):
        yield documents[i:i + batch_size]

def create_or_load_vectorstore(documents):
    embeddings = get_embeddings()
    
    # First batch
    batches = list(batch_documents(documents))
    vectorstore = FAISS.from_documents(batches[0], embeddings)

    # Add other batches
    for batch in batches[1:]:
        vectorstore.add_documents(batch)

    vectorstore.save_local(VECTOR_DB_PATH)
    return vectorstore
