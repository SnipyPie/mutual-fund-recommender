import pandas as pd

def feature_engineering(df):
    risk_free_rate = 0.06

    df['sharpe_calc'] = (df['returns_3yr'] - risk_free_rate) / df['sd']

    df['return_score'] = df['returns_3yr']
    df['risk_score'] = df['sd']
    df['expense_penalty'] = df['expense_ratio']

    return df

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned_funds.csv")
    df = feature_engineering(df)
    df.to_csv("data/features.csv", index=False)
    print("Features created successfully")