# 🚀 Intelligent Mutual Fund Recommendation & Prediction System

An end-to-end machine learning system that recommends the best mutual funds based on user preferences and predicts future returns using advanced ML models.

---

## 🌐 Live Demo

frontend:- https://mutual-fund-recommender-system.streamlit.app/
backend:- https://mutual-fund-recommender-yn2f.onrender.com/

---

## 💡 Problem Statement

Choosing the right mutual fund is complex due to multiple financial factors like risk, returns, and fund performance.

This system simplifies decision-making by:
- Recommending top funds based on user profile
- Predicting future returns using ML

---

## ⚙️ Features

- 🎯 Personalized recommendations (risk + duration)
- 📊 Financial scoring system (Sharpe, risk, returns)
- 🤖 ML-based return prediction (1Y, 3Y, 5Y)
- 🔌 FastAPI backend for scalable architecture
- 🌐 Fully deployed frontend + backend system
- ⚡ Real-time interaction with API

---

## 🏗️ System Architecture


```
User Input (Risk, Duration)
↓
Streamlit Frontend (Cloud)
↓
FastAPI Backend (Render)
↓
Recommendation Engine (Scoring)
↓
Top 5 Mutual Funds
↓
User Selection
↓
ML Model (Gradient Boosting)
↓
Predicted Returns (1Y, 3Y, 5Y)
```

---

## 🧠 Machine Learning Approach

- Performed EDA (correlation, distribution, feature relationships)
- Compared models:
  - Linear Regression (baseline)
  - Random Forest
  - Gradient Boosting (final model)
- Selected Gradient Boosting based on:
  - Higher R² score
  - Lower MAE
  - Better handling of non-linearity

---

## 🛠️ Tech Stack

**Frontend:**
- Streamlit

**Backend:**
- FastAPI

**Machine Learning:**
- Scikit-learn
- Pandas, NumPy

**Deployment:**
- Render (Backend)
- Streamlit Cloud (Frontend)

---

## 📸 Application Preview

![App Screenshot](screenshot.png)

---

## 📂 Project Structure
mutual-fund-recommender/
│
├── app/ # Streamlit frontend
├── api/ # FastAPI backend
├── src/ # ML + recommendation logic
├── data/ # datasets
├── requirements.txt
├── README.md

---

## 🚀 Future Improvements

- 🤖 AI-based explanation using LLMs
- 🗄️ Database integration (PostgreSQL)
- 📡 Real-time financial data pipeline
- 📊 Advanced analytics dashboard

---

## 🧠 Key Learnings

- Built a complete ML pipeline from scratch
- Designed scalable backend using FastAPI
- Integrated ML models into production system
- Handled real-world issues like API latency and state management

---

## 👨‍💻 Author

Shrijan  
GitHub: https://github.com/SnipyPie
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



```
![App Screenshot]
### 🔹 Recommendation System
![Recommendation](screenshots/img1.png)
### 🔹 Fund Selection
![Selection](screenshots/img2.png)
### 🔹 ML Prediction Output
![Prediction](screenshots/img3.png)
```

