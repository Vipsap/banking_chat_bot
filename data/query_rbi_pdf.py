import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from data.rbi_table_chart_functions import *

# ======================= 🌍 GLOBAL BANKING FUNCTIONS =======================

def get_npl_ratio_by_country():
    """Returns Non-Performing Loan (NPL) ratio by country."""
    return pd.read_csv("data/npl_ratio_by_country.csv")

def get_provision_coverage_ratio():
    """Returns Provision Coverage Ratios across countries."""
    return pd.read_csv("data/provision_coverage_ratio.csv")

def get_risk_weighted_assets_by_country():
    """Returns CRAR - Capital to Risk-weighted Assets Ratio by country."""
    return pd.read_csv("data/risk_weighted_assets.csv")

def get_tier1_capital_by_country():
    """Returns Tier 1 capital ratios by country."""
    return pd.read_csv("data/tier1_by_country.csv")

def get_global_banks_by_total_assets():
    """Returns a table of the largest banks globally by total assets."""
    return pd.read_csv("data/global_banks_by_assets.csv")


# ======================= 📈 PLOT FUNCTIONS (Chart Extraction) =======================

def plot_inflation_trend_chart():
    """Shows inflation chart extracted from Chart II.1b."""
    st.image("images/chart_inflation_trend.png", caption="Chart II.1b: Inflation Trend by Country")

def plot_monetary_policy_chart():
    """Shows monetary policy chart extracted from Chart II.2a and II.2b."""
    st.image("images/chart_monetary_policy_rates.png", caption="Chart II.2a & II.2b: Monetary Policy Rates")

def plot_gdp_growth_chart():
    """Shows global GDP growth trend between EMDEs and AEs."""
    st.image("images/chart_gdp_growth.png", caption="GDP Growth Trend: EMDEs vs AEs")


# ======================= 🇮🇳 INDIAN BANKING FUNCTIONS =======================

def get_domestic_credit_growth():
    """Returns domestic credit growth across bank groups."""
    return pd.read_csv("data/domestic_credit_growth.csv")

def get_psb_vs_pvb_balance_share():
    """Returns comparison of balance share between PSBs and PVBs."""
    return pd.read_csv("data/psb_pvb_balance_share.csv")

def get_top_banks_by_net_profit():
    """Returns top Indian banks by net profit."""
    return pd.read_csv("data/top_banks_by_net_profit.csv")

def get_top_banks_by_nii():
    """Returns top Indian banks by net interest income."""
    return pd.read_csv("data/top_banks_by_nii.csv")

def get_banks_by_crar():
    """Returns banks sorted by CRAR values."""
    return pd.read_csv("data/indian_banks_crar.csv")

def get_psb_npa_comparison():
    """Returns PSB vs PVB comparison for NPA levels."""
    return pd.read_csv("data/psb_pvb_npa_comparison.csv")

def get_operating_profit_trend():
    """Returns operating profit trend for major bank groups."""
    return pd.read_csv("data/operating_profit_trend.csv")

def get_technology_adoption_trend():
    """Returns tech adoption trends like UPI, NEFT, etc."""
    return pd.read_csv("data/technology_adoption_trend.csv")


# ======================= 🧾 ADDITIONAL METRICS =======================

def get_cash_balances_with_rbi():
    """Returns cash balances maintained by banks with RBI."""
    return pd.read_csv("data/cash_with_rbi.csv")

def get_total_liabilities_ratio():
    """Returns liabilities to assets ratios across banks."""
    return pd.read_csv("data/liabilities_ratio.csv")

def get_capital_adequacy_indicators():
    """Returns indicators like CRAR, Tier 1 and leverage ratios."""
    return pd.read_csv("data/capital_adequacy_indicators.csv")

def get_deposit_liability_by_group():
    """Returns deposit liabilities split by bank group (PSB, PVB, etc.)."""
    return pd.read_csv("data/deposit_liabilities_by_group.csv")
