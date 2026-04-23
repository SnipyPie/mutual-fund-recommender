# 🚀 Mutual Fund Recommendation & Prediction System

An intelligent system that recommends optimal mutual funds based on user profile and predicts future returns using Machine Learning.

---

## 🧠 Problem Statement

Investors often struggle to select the right mutual funds due to complex financial metrics and lack of personalized insights.

This system solves that by:

* Recommending funds based on risk appetite and investment duration
* Predicting future returns using ML models

---

## 🔄 System Flow

```
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
```

---

## ⚙️ Features

* 🔍 Data preprocessing and cleaning pipeline
* 📊 Feature engineering using financial metrics (Sharpe ratio, risk, returns, expense ratio)
* 🧮 Scoring engine to rank mutual funds
* 🎯 Personalized recommendations based on:

  * Risk level (Low, Medium, High)
  * Investment duration (Short, Medium, Long)
* 🤖 Machine Learning model for return prediction (Gradient Boosting)
* 🌐 Interactive Streamlit web application

---

## 🏗️ Architecture

```
Frontend (Streamlit)
        ↓
FastAPI Backend
        ↓
Recommendation Engine + ML Model
        ↓
Data Layer (CSV → Future DB)
```

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn (Random Forest, Gradient Boosting)
* Streamlit
* FastAPI
* SQL
* Matplotlib

---

## 🚀 How to Run

```bash
git clone https://github.com/SnipyPie/mutual-fund-recommender.git
cd mutual-fund-recommender

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

# Run backend
uvicorn api.main:app --reload

# Run frontend (in another terminal)
streamlit run app/app.py
```

---

## 📸 Application Preview

(Add your screenshot here)

```
![App Screenshot](screenshot.png)
```

---

## 🌐 Live Demo

(Will be added after deployment)

---

## 🚀 Future Improvements

* Integration with real-time financial APIs
* Database integration (PostgreSQL)
* LLM-based explanations (“Why this fund?”)
* Full production deployment

---

## 👨‍💻 Author

**SnipyPie**