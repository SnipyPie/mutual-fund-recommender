import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src.recommend import recommend
from src.predict import predict_returns

st.title("Mutual Fund Recommendation System")
st.markdown("### Get personalized mutual fund recommendations based on your profile")

# User Inputs
risk = st.selectbox("Select Risk Level", ["Low", "Medium", "High"])
duration = st.selectbox("Investment Duration", ["Short", "Medium", "Long"])

if "result" not in st.session_state:
    st.session_state.result = None

# Recommend button
if st.button("Recommend"):
    result = recommend(risk, duration)
    st.session_state.result = result

# Show result if exists
if st.session_state.result is not None:
    result = st.session_state.result

    if "message" in result.columns:
        st.warning(result["message"].iloc[0])
    else:
        st.subheader("Top Recommended Funds")
        st.dataframe(result.reset_index(drop=True))

        # Load full data
        df_full = pd.read_csv("data/cleaned_funds.csv")

        # Select fund
        selected_fund = st.selectbox(
            "Select a fund to predict returns",
            result['scheme_name'],
            key="fund_select"
        )

        # Predict button
        if st.button("Predict Returns"):
            fund_row = df_full[df_full['scheme_name'] == selected_fund].iloc[0]

            prediction = predict_returns(fund_row)

            st.subheader("Predicted Returns")
            st.write(f"1 Year Return: {round(prediction['1Y'], 2)}%")
            st.write(f"3 Year Return: {round(prediction['3Y'], 2)}%")
            st.write(f"5 Year Return: {round(prediction['5Y'], 2)}%")