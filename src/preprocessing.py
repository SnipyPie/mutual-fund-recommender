import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()

    numeric_cols = [
        'expense_ratio', 'fund_size_cr', 'fund_age_yr',
        'sortino', 'alpha', 'sd', 'beta', 'sharpe',
        'returns_1yr', 'returns_3yr', 'returns_5yr'
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.dropna()

    return df

if __name__ == "__main__":
    df = load_data("data/mutual_funds.csv")
    df = clean_data(df)
    df.to_csv("data/cleaned_funds.csv", index=False)
    print("Data cleaned successfully")