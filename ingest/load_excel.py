from langchain_community.document_loaders import UnstructuredExcelLoader
import pandas as pd
from langchain.schema import Document

def load_excel_documents(excel_path="data/Indian Banking Data.xlsx"):
    dfs = pd.read_excel(excel_path, sheet_name=None)  # Load all sheets
    docs = []

    for sheet, df in dfs.items():
        if df.empty:
            continue

        # Convert the table to markdown format for display
        markdown_table = df.head(20).to_markdown(index=False)  # Limit rows if needed

        doc = Document(
            page_content=markdown_table,
            metadata={"source": f"{excel_path} [{sheet}]"}
        )
        docs.append(doc)

    return docs
# This function loads Excel documents from a specified path.
# It reads all sheets, converts the first 20 rows of each sheet to markdown format,