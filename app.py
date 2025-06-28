import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import data.query_rbi_pdf as pdf
import data.query_excel as qx

from ingest.load_pdf import load_pdf_documents
from ingest.load_excel import load_excel_documents
from utils.chunker import split_documents
from vectorstore.create_store import create_or_load_vectorstore
from agent.banking_agent import load_agent

st.set_page_config(page_title="📊 Indian Banking ChatBot", layout="wide")
st.title("🤖 Indian Banking Knowledge ChatBot")

# Session State for History
if "history" not in st.session_state:
    st.session_state.history = []

if "agent" not in st.session_state:
    st.session_state.agent = None

# Sidebar
st.sidebar.title("📁 Options")
if st.sidebar.button("🔄 Reset Chat"):
    st.session_state.history = []

st.sidebar.markdown("Made by Vipan with ❤️")

# Load vector DB if not already present
if not os.path.exists("vectorstore/banking_faiss/index.faiss"):
    with st.spinner("🧠 Processing documents..."):
        docs = load_pdf_documents() + load_excel_documents()
        chunks = split_documents(docs)
        create_or_load_vectorstore(chunks)
        st.success("✅ Vectorstore created.")

# Load LLM Agent
if st.session_state.agent is None:
    st.session_state.agent = load_agent()
qa_chain = st.session_state.agent

# 🔍 Unified Structured Query Handler (Excel + PDF)
def handle_structured_queries(query):
    import data.rbi_table_chart_functions as rbi

    q = query.lower()

    # === Auto-match Tables ===
    for i in range(1, 141):
        table_code = f"table {i}"
        if table_code in q or f"table_{i:03}" in q or f"table{i:03}" in q:
            func_name = f"get_table_{i:03}"
            if hasattr(rbi, func_name):
                return getattr(rbi, func_name)()

    # === Auto-match Charts ===
    for j in range(1, 86):
        chart_code = f"chart {j}"
        if chart_code in q or f"chart_{j:03}" in q or f"chart{j:03}" in q:
            func_name = f"plot_chart_{j:03}"
            if hasattr(rbi, func_name):
                getattr(rbi, func_name)()  # Plot directly

    # === PDF Structured CSV Queries ===
    if "npl ratio" in q or "asset quality" in q:
        return pdf.get_npl_ratio_by_country()

    if "provision coverage" in q or "pcr" in q:
        return pdf.get_provision_coverage_ratio()

    if "risk-weighted" in q and "country" in q:
        return pdf.get_risk_weighted_assets_by_country()

    if "tier 1 capital" in q:
        return pdf.get_tier1_capital_by_country()

    if "largest global banks" in q or "banks by assets" in q:
        return pdf.get_global_banks_by_total_assets()

    if "domestic credit" in q:
        return pdf.get_domestic_credit_growth()

    if "psb vs pvb" in q or "balance share" in q:
        return pdf.get_psb_vs_pvb_balance_share()

    if "banks by crar" in q or "crar value" in q:
        return pdf.get_banks_by_crar()

    if "psb npa" in q or "npa comparison" in q:
        return pdf.get_psb_npa_comparison()

    if "operating profit" in q:
        return pdf.get_operating_profit_trend()

    if "technology adoption" in q or "upi" in q or "fintech" in q:
        return pdf.get_technology_adoption_trend()

    if "cash with rbi" in q:
        return pdf.get_cash_balances_with_rbi()

    if "liabilities ratio" in q or "total liabilities" in q:
        return pdf.get_total_liabilities_ratio()

    if "deposit liabilities" in q:
        return pdf.get_deposit_liability_by_group()

    if "capital adequacy" in q:
        return pdf.get_capital_adequacy_indicators()

    # === PDF Charts ===
    if "inflation chart" in q or "chart ii.1b" in q:
        pdf.plot_inflation_trend_chart()
        return None

    if "monetary policy chart" in q or "chart ii.2" in q:
        pdf.plot_monetary_policy_chart()
        return None

    if "gdp growth chart" in q:
        pdf.plot_gdp_growth_chart()
        return None

    # === Excel Queries ===
    if "top 5" in q and "net profit" in q:
        return qx.get_top_5_banks_by_nii()

    if any(k in q for k in ["highest roa", "best roa", "maximum roa", "top roa", "high roa"]):
        return qx.get_highest_roa_banks()

    if any(k in q for k in ["lowest roa", "minimum roa", "worst roa", "low roa"]):
        return qx.get_lowest_roa_banks()

    if "average roa" in q or "mean roa" in q:
        avg = qx.get_average_roa()
        return pd.DataFrame([{"Average ROA (%)": f"{avg:.2f}%"}]) if avg else None

    if "highest npa" in q: return qx.get_highest_npa_provision()
    if "highest deposit ratio" in q: return qx.get_highest_deposit_ratio()
    if "total staff" in q: return qx.get_highest_staff_banks()
    if "roa risk" in q: return qx.get_best_roa_risk_banks()
    if "operating income" in q: return qx.get_highest_opinc_ratio()
    if "loan ratio" in q: return qx.get_highest_loan_ratio()
    if "equity ratio" in q: return qx.get_highest_equity_ratio()
    if "largest banks" in q or "total assets" in q: return qx.get_largest_banks_by_assets()
    if "asset growth" in q: return qx.get_highest_asset_growth()
    if "diversification" in q: return qx.get_most_diverse_banks()
    if "risky banks" in q: return qx.get_riskiest_banks()
    if "govt expenditure" in q or "government spending" in q: return qx.get_highest_gov_exp_banks()
    if "inflation impact" in q: return qx.get_highest_inflation_exposed()
    if "hhi nii" in q: return qx.get_highest_hhi_nii()
    if "gdp exposure" in q: return qx.get_highest_gdp_grth_exposure()
    if "repo sensitive" in q: return qx.get_most_repo_sensitive()
    if "gfce exposure" in q: return qx.get_highest_gfce_exposure()
    if "financial summary" in q: return qx.get_financial_summary_table()

    return None

# 📈 Chart Plot
def plot_roa_vs_loan(excel_df):
    st.subheader("📉 ROA vs Loan Ratio Chart")
    df = excel_df.copy()
    if 'ROA (%)' in df.columns and 'Loan Ratio (%)' in df.columns:
        df['ROA'] = df['ROA (%)'].str.rstrip('%').astype(float)
        df['Loan Ratio'] = df['Loan Ratio (%)'].str.rstrip('%').astype(float)
        fig, ax = plt.subplots()
        ax.scatter(df['ROA'], df['Loan Ratio'], color='green')
        ax.set_xlabel("ROA (%)")
        ax.set_ylabel("Loan Ratio (%)")
        ax.set_title("ROA vs Loan Ratio of Top Banks")
        st.pyplot(fig)

# 💬 Main Chat Interface
query = st.text_input("💬 Ask a banking-related question:")

if query:
    structured_answer = handle_structured_queries(query)

    if structured_answer is not None:
        st.subheader("📊 Answer from Excel/PDF Data")
        st.dataframe(structured_answer, use_container_width=True)

        plot_roa_vs_loan(structured_answer)

        st.download_button("📥 Download Table as CSV",
                           data=structured_answer.to_csv(index=False).encode('utf-8'),
                           file_name="summary_table.csv",
                           mime='text/csv')

        st.session_state.history.append({
            "query": query,
            "answer": structured_answer.to_csv(index=False),
            "source": "Structured"
        })

    else:
        with st.spinner("Searching in PDF knowledge base..."):
            result = qa_chain(query)
            answer = result["result"]
            sources = result["source_documents"]

            st.subheader("🤖 Answer from LLM")
            st.write(answer)

            st.subheader("📄 Sources")
            for src in sources:
                if src.page_content.startswith("|"):
                    st.markdown(src.page_content)
                else:
                    st.markdown(f"> {src.page_content[:300]}...")

            st.session_state.history.append({
                "query": query,
                "answer": answer,
                "source": sources
            })

# 🕒 Chat History in Sidebar
if st.sidebar.checkbox("🕒 Show Chat History"):
    for i, chat in enumerate(reversed(st.session_state.history)):
        st.sidebar.markdown(f"**Q{i+1}:** {chat['query']}")
        if isinstance(chat["answer"], str):
            st.sidebar.markdown(f"*A:* {chat['answer'][:200]}...")
        else:
            st.sidebar.write(chat["answer"])
