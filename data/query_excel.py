import pandas as pd

# Load once when app starts
xls = pd.ExcelFile("data/Indian Banking Data.xlsx")
sheet1 = xls.parse('Sheet1')
sheet2 = xls.parse('Sheet2')

# Shared filter: latest year
def latest_year(df):
    return df[df['year'] == df['year'].max()]

# --- Core Functions ---

def get_top_5_banks_by_nii():
    df = sheet2[['bank', 'year', 'nii']].dropna()
    df = latest_year(df)
    return df.sort_values(by='nii', ascending=False).head(5).reset_index(drop=True)

def get_highest_roa_banks():
    df = sheet2[['bank', 'year', 'roa']].dropna()
    df = latest_year(df)
    return df.sort_values(by='roa', ascending=False).head(5).reset_index(drop=True)

def get_lowest_roa_banks():
    df = sheet2[['bank', 'year', 'roa']].dropna()
    df = latest_year(df)
    return df.sort_values(by='roa', ascending=True).head(5).reset_index(drop=True)

def get_average_roa():
    df = sheet2[['year', 'roa']].dropna()
    df = latest_year(df)
    return df['roa'].mean()

def get_highest_npa_provision():
    df = sheet2[['bank', 'year', 'prov_npa']].dropna()
    df = latest_year(df)
    return df.sort_values(by='prov_npa', ascending=False).head(5).reset_index(drop=True)

def get_highest_deposit_ratio():
    df = sheet2[['bank', 'year', 'dep_ratio']].dropna()
    df = latest_year(df)
    return df.sort_values(by='dep_ratio', ascending=False).head(5).reset_index(drop=True)

def get_highest_staff_banks():
    df = sheet2[['bank', 'year', 'total_staff']].dropna()
    df = latest_year(df)
    return df.sort_values(by='total_staff', ascending=False).head(5).reset_index(drop=True)

def get_best_roa_risk_banks():
    df = sheet2[['bank', 'year', 'roa_risk']].dropna()
    df = latest_year(df)
    return df.sort_values(by='roa_risk', ascending=False).head(5).reset_index(drop=True)

def get_highest_opinc_ratio():
    df = sheet2[['bank', 'year', 'nii_opinc']].dropna()
    df = latest_year(df)
    return df.sort_values(by='nii_opinc', ascending=False).head(5).reset_index(drop=True)

def get_highest_loan_ratio():
    df = sheet2[['bank', 'year', 'loanratio']].dropna()
    df = latest_year(df)
    return df.sort_values(by='loanratio', ascending=False).head(5).reset_index(drop=True)

def get_highest_equity_ratio():
    df = sheet2[['bank', 'year', 'equityratio']].dropna()
    df = latest_year(df)
    return df.sort_values(by='equityratio', ascending=False).head(5).reset_index(drop=True)

def get_largest_banks_by_assets():
    df = sheet2[['bank', 'year', 'log_ta']].dropna()
    df = latest_year(df)
    return df.sort_values(by='log_ta', ascending=False).head(5).reset_index(drop=True)

def get_highest_asset_growth():
    df = sheet2[['bank', 'year', 'tagr']].dropna()
    df = latest_year(df)
    return df.sort_values(by='tagr', ascending=False).head(5).reset_index(drop=True)

def get_most_diverse_banks():
    df = sheet2[['bank', 'year', 'diverse']].dropna()
    df = latest_year(df)
    return df.sort_values(by='diverse', ascending=False).head(5).reset_index(drop=True)

def get_riskiest_banks():
    df = sheet2[['bank', 'year', 'roa_risk_5yr']].dropna()
    df = latest_year(df)
    return df.sort_values(by='roa_risk_5yr', ascending=True).head(5).reset_index(drop=True)

def get_highest_gov_exp_banks():
    df = sheet2[['bank', 'year', 'govt_exp']].dropna()
    df = latest_year(df)
    return df.sort_values(by='govt_exp', ascending=False).head(5).reset_index(drop=True)

def get_highest_inflation_exposed():
    df = sheet2[['bank', 'year', 'inflation']].dropna()
    df = latest_year(df)
    return df.sort_values(by='inflation', ascending=False).head(5).reset_index(drop=True)

def get_highest_hhi_nii():
    df = sheet2[['bank', 'year', 'hhi_nii']].dropna()
    df = latest_year(df)
    return df.sort_values(by='hhi_nii', ascending=False).head(5).reset_index(drop=True)

def get_highest_gdp_grth_exposure():
    df = sheet2[['bank', 'year', 'gdp_grth']].dropna()
    df = latest_year(df)
    return df.sort_values(by='gdp_grth', ascending=False).head(5).reset_index(drop=True)

def get_most_repo_sensitive():
    df = sheet2[['bank', 'year', 'repo']].dropna()
    df = latest_year(df)
    return df.sort_values(by='repo', ascending=False).head(5).reset_index(drop=True)

def get_highest_gfce_exposure():
    df = sheet2[['bank', 'year', 'gfce']].dropna()
    df = latest_year(df)
    return df.sort_values(by='gfce', ascending=False).head(5).reset_index(drop=True)

# Financial Summary
def get_financial_summary_table():
    required_columns = [
        'bank', 'sector', 'year', 'nii', 'roa', 'dep_ratio', 'prov_npa',
        'total_staff', 'inflation', 'roa_risk', 'nii_opinc', 'loanratio',
        'equityratio', 'log_ta', 'tagr', 'gdp_grth', 'gfce',
        'roa_risk_5yr', 'govt_exp', 'repo', 'hhi_nii', 'diverse'
    ]
    
    missing = [col for col in required_columns if col not in sheet2.columns]
    if missing:
        return pd.DataFrame([{"error": f"Missing columns in Excel: {', '.join(missing)}"}])

    df = sheet2[required_columns].copy()
    df = latest_year(df).dropna(subset=['bank'])
    df = df.drop_duplicates().sort_values(by='nii', ascending=False).head(15)

    df = df.rename(columns={
        'bank': 'Bank Name',
        'sector': 'Bank Type',
        'year': 'Year',
        'nii': 'Net Interest Income (₹ Cr)',
        'roa': 'ROA (%)',
        'dep_ratio': 'Deposit Ratio (%)',
        'prov_npa': 'Provision for NPAs (%)',
        'total_staff': 'Staff Count',
        'inflation': 'Inflation (%)',
        'roa_risk': 'ROA Risk (1Y)',
        'nii_opinc': 'NII / Operating Income (%)',
        'loanratio': 'Loan Ratio (%)',
        'equityratio': 'Equity Ratio (%)',
        'log_ta': 'Log(Total Assets)',
        'tagr': 'Asset Growth Rate (%)',
        'gdp_grth': 'GDP Growth Exposure (%)',
        'gfce': 'Govt Final Consumption Exposure (%)',
        'roa_risk_5yr': 'ROA Risk (5Y)',
        'govt_exp': 'Government Expenditure (%)',
        'repo': 'Repo Rate (%)',
        'hhi_nii': 'HHI (NII)',
        'diverse': 'Diversification Score'
    })

    percent_cols = [
        'ROA (%)', 'Deposit Ratio (%)', 'Provision for NPAs (%)', 'Inflation (%)',
        'ROA Risk (1Y)', 'NII / Operating Income (%)', 'Loan Ratio (%)',
        'Equity Ratio (%)', 'Asset Growth Rate (%)', 'GDP Growth Exposure (%)',
        'Govt Final Consumption Exposure (%)', 'ROA Risk (5Y)',
        'Government Expenditure (%)', 'Repo Rate (%)'
    ]

    for col in percent_cols:
        df[col] = df[col].apply(lambda x: f"{x:.2f}%" if pd.notnull(x) else "N/A")

    return df.reset_index(drop=True)
