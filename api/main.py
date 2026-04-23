from fastapi import FastAPI
import pandas as pd
import joblib

from src.recommend import recommend
from src.predict import predict_returns

app = FastAPI()
@app.get("/")
def home():
    return {"message":"mutual fund API is running"}

@app.get("/recommend")
def get_recommendation(risk: str,duration: str):
    result=recommend(risk,duration)
    return result.to_dict(orient="records")

@app.get("/predict")
def predict(fund_name: str):
    df = pd.read_csv("data/cleaned_funds.csv")
    fund_row = df[df['scheme_name'] == fund_name].iloc[0]
    prediction = predict_returns(fund_row)
    return prediction