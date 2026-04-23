# 🚀 Mutual Fund Recommendation & Prediction System

An intelligent system that recommends top mutual funds based on user profile and predicts future returns using Machine Learning.



\---



## 🧠 Problem Statement

Investors often struggle to select the right mutual funds due to complex financial metrics and lack of personalized insights.

This project solves that by:
- Recommending optimal funds based on risk and duration
- Predicting future returns using ML models



\---

## 🔄 System Flow
User Input (Risk, Duration)
↓
Recommendation Engine (Scoring System)
↓
Top 5 Mutual Funds
↓
User Selection
↓
ML Prediction Model (Gradient Boosting)
↓
Predicted Returns (1Y, 3Y, 5Y)

\## ⚙️ Features



\- 🔍 Data preprocessing and cleaning pipeline  

\- 📊 Feature engineering using financial metrics (Sharpe ratio, returns, risk, expense ratio)  

\- 🧮 Scoring engine to rank mutual funds  

\- 🎯 Personalized recommendations based on:

&#x20; - Risk level (Low, Medium, High)

&#x20; - Investment duration (Short, Medium, Long)  

\- 💡 Explainable AI: Provides reasoning behind each recommendation  

\- 🌐 Interactive Streamlit web application  



\---



\## 🏗️ Architecture

User Input → Recommendation Engine → Scoring System → Feature Engineering → Clean Data
---



## ⚙️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn (Random Forest, Gradient Boosting)  
- Streamlit  
- SQL  
- Matplotlib  



\---



## 🚀 How to Run

```bash
git clone https://github.com/SnipyPie/mutual-fund-recommender.git
cd mutual-fund-recommender

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app/app.py



pip install -r requirements.txt



streamlit run app/app.py

