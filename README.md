# 📊 Indian Banking ChatBot 🤖🇮🇳

This is a **Streamlit-based intelligent chatbot** built to answer **data-driven questions** about the Indian banking sector using **RBI Trend and Progress in Banking Reports** and **structured Excel datasets**. It supports both **natural language queries** and **interactive data exploration**.

---

## 📁 Features

- ✅ **Chatbot UI** powered by Streamlit  
- 📊 **Excel-based banking queries** (CRAR, ROA, NII, loan ratio, inflation exposure, etc.)  
- 🤖 **LLM Agent fallback** for generic banking questions  
- 🧠 **Vector DB (FAISS)** for document retrieval using LangChain  

---

## 📦 Project Structure

```bash
Banking Chat Bot/
│
├── app.py                          # Main Streamlit app
├── README.md                       # You are here!
│
├── data/
│   ├── Indian Banking Data.xlsx    # Excel file with banking KPIs
│   ├── table_001.csv ... 140       # RBI tables (manually linked)
│   └── rbi_table_chart_functions.py # All functions to retrieve table/chart
│
├── images/
│   └── chart_001.png ... chart_085.png  # RBI chart images
│
├── ingest/
│   ├── load_pdf.py                 # PDF loader
│   └── load_excel.py               # Excel loader
│
├── vectorstore/
│   └── banking_faiss/              # FAISS index
│
├── agent/
│   └── banking_agent.py           # LangChain agent setup
│
├── utils/
│   └── chunker.py                 # PDF chunking utility



## Setup Instructions

Create a VENV env in your local 

pip install -r requirements.txt


## Run the App

streamlit run app.py


## How It Works
Natural language queries are passed to handle_structured_queries() in app.py

It matches to a function in:

query_excel.py for Excel-based KPIs

query_rbi_pdf.py or rbi_table_chart_functions.py for Tables/Charts

If not matched, fallback to LLM QA over PDF using LangChain


## Ask any of the following in your chatbot:

Top banks:

"Which are the top 5 banks by net interest income?"

"Show banks with highest ROA"

"List banks with lowest ROA"

"Give average ROA of all banks"

## Risk and performance:

"Banks with highest provision for NPAs"

"Who has the highest deposit ratio?"

"Banks with highest loan ratio"

"Show highest equity ratio banks"

"Banks with highest asset growth"

"Top diversified banks"

"Banks with lowest risk-adjusted ROA"

## Economic exposure:

"Which banks are most exposed to government spending?"

"Banks most sensitive to inflation"

"Show banks with highest GDP growth exposure"

"Who are the most repo-sensitive banks?"

## Clone the Repo

git clone https://github.com/Vipsap/banking_chat_bot.git
cd banking_chat_bot

##Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows


## Install dependencies
pip install -r requirements.txt

## Powered By
LangChain

Agents AI

OpenAI API

FAISS / ChromaDB

Streamlit


