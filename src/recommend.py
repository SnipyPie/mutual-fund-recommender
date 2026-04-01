import pandas as pd

def recommend(risk_level, duration):
    df = pd.read_csv("data/scored.csv")

    #Risk Filtering
    if risk_level == "Low":
        df = df[df['risk_level'] <= 2]
    elif risk_level == "Medium":
        df = df[(df['risk_level'] >= 3) & (df['risk_level'] <= 4)]
    elif risk_level == "High":
        df = df[df['risk_level'] >= 5]
    
    #Duration Filtering
    if duration == "Short":
        df = df[df['category'].str.contains("Debt", case=False)]
    elif duration == "Medium":
        df = df[df['category'].str.contains("Hybrid", case=False)]
    elif duration == "Long":
        df = df[df['category'].str.contains("Equity", case=False)]
    #Handle empty result
    if df.empty:
    # fallback: relax risk filter
        df = pd.read_csv("data/scored.csv")

        if duration == "Short":
            df = df[df['category'].str.contains("Debt", case=False)]
        elif duration == "Medium":
            df = df[df['category'].str.contains("Hybrid", case=False)]
        elif duration == "Long":
            df = df[df['category'].str.contains("Equity", case=False)]

    #Ranking
    df = df.sort_values(by="final_score", ascending=False)

    top = df.head(5)

    def explain(row):
        if row['sharpe_calc'] > 1:
            return "High return with good risk-adjusted performance"
        elif row['risk_score'] < 10:
            return "Low risk and stable returns"
        else:
            return "Balanced risk and return"

    top['explanation'] = top.apply(explain, axis=1)

    return top[['scheme_name', 'category', 'final_score', 'explanation']]


if __name__ == "__main__":
    result = recommend("Low", "Long")
    print(result)