import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.recommend import recommend

st.title("Mutual Fund Recommendation System")
st.markdown("### Get personalized mutual fund recommendations based on your profile")

# User Inputs
risk = st.selectbox("Select Risk Level", ["Low", "Medium", "High"])
duration = st.selectbox("Investment Duration", ["Short", "Medium", "Long"])

# Button
if st.button("Recommend"):
    result = recommend(risk, duration)

    if "message" in result.columns:
        st.warning(result["message"].iloc[0])
    else:
        st.subheader("Top Recommended Funds")

        #  Metrics
        col1, col2, col3 = st.columns(3)

        col1.metric("Funds Selected", len(result))
        col2.metric("Avg Score", round(result['final_score'].mean(), 2))
        col3.metric("Category", result['category'].iloc[0])

        st.dataframe(result.reset_index(drop=True))