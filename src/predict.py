import pandas as pd
import joblib

# Load model
model = joblib.load("models/gbr_model.pkl")

def predict_returns(fund_row):
    features = [
        'expense_ratio',
        'fund_size_cr',
        'fund_age_yr',
        'alpha',
        'beta',
        'sharpe',
        'rating',
        'risk_level'
    ]

    X = fund_row[features].values.reshape(1, -1)

    prediction = model.predict(X)[0]

    return {
        "1Y": prediction[0],
        "3Y": prediction[1],
        "5Y": prediction[2]
    }