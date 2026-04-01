import pandas as pd

def calculate_score(df):
    df['final_score'] = (
        0.4 * df['sharpe_calc'] +
        0.3 * df['return_score'] -
        0.2 * df['risk_score'] -
        0.1 * df['expense_penalty']
    )
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/features.csv")
    df = calculate_score(df)
    df.to_csv("data/scored.csv", index=False)
    print("Scoring completed successfully")