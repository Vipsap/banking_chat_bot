from langchain_community.document_loaders import PyPDFLoader


def load_pdf_documents(pdf_path="data/Indian Banking RBI Data.pdf"):
    loader = PyPDFLoader(pdf_path)
    return loader.load()
