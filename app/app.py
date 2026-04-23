import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src.recommend import recommend
from src.predict import predict_returns
import requests
st.title("Mutual Fund Recommendation System")
st.markdown("### Get personalized mutual fund recommendations based on your risk profile and investment duration")
st.info("This system uses financial metrics + machine learning to recommend and predict fund performance.")

API_URL = "http://127.0.0.1:8000"

# User Inputs
risk = st.selectbox("Select Risk Level", ["Low", "Medium", "High"])
duration = st.selectbox("Investment Duration", ["Short", "Medium", "Long"])

if "result" not in st.session_state:
    st.session_state.result = None

# Recommend button
if st.button("Recommend"):
    response = requests.get(
        f"{API_URL}/recommend",
        params={"risk": risk, "duration": duration}
    )
    st.session_state.result = pd.DataFrame(response.json())

# Show result if exists
if st.session_state.result is not None:
    result = st.session_state.result

    if "message" in result.columns:
        st.warning(result["message"].iloc[0])
    else:
        st.subheader("Top Recommended Funds")
        st.dataframe(result.reset_index(drop=True), use_container_width=True)
        import matplotlib.pyplot as plt

        st.subheader("Fund Score Comparison")

        fig, ax = plt.subplots()
        ax.bar(result['scheme_name'], result['final_score'])

        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

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
            response = requests.get(
                f"{API_URL}/predict",
                params={"fund_name": selected_fund}
            )

            prediction = response.json()

            col1, col2, col3 = st.columns(3)
            col1.metric("1 Year Return", f"{round(prediction['1Y'], 2)}%")
            col2.metric("3 Year Return", f"{round(prediction['3Y'], 2)}%")
            col3.metric("5 Year Return", f"{round(prediction['5Y'], 2)}%")