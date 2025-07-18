# 💧 Water Quality Analysis using Machine Learning

## 📌 Project Overview

This project aims to analyze water quality data and predict whether a water sample is **drinkable** or **not** using various Machine Learning models. The dataset includes key parameters like pH, Temperature and more. The final model can help government bodies and laboratories quickly assess water safety, especially in areas with limited testing resources.

---

## 📂 Table of Contents

- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [Problem Statement](#-problem-statement)
- [Technologies Used](#-technologies-used)
- [Models Implemented](#-models-implemented)
- [Data Preprocessing](#-data-preprocessing)
- [Model Evaluation](#-model-evaluation)
- [Flask Web App](#-flask-web-app)
- [How to Run](#-how-to-run)
- [Results](#-results)
- [Future Scope](#-future-scope)

---

## 📊 Dataset

- **Source:** [HydroShare Dataset](https://www.hydroshare.org/resource/4ab43e1b507b496b9b42749701daed5c/)
- **Features:**
  - Temperature  
  - D.O. (Dissolved Oxygen)  
  - pH  
  - Conductivity  
  - B.O.D (Biochemical Oxygen Demand)  
  - Nitrate  
  - Fecal Coliform  
  - Total Coliform  
  - **Potability** (Target: 0 = Not drinkable, 1 = Drinkable)

---

## ❓ Problem Statement

> Develop a machine learning model that can predict the **potability** of water based on its physical and chemical characteristics.

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn  
- **Web Framework:** Flask  
- **Frontend:** HTML, CSS, Bootstrap

---

## 🤖 Models Implemented

- Linear Regression  
- Support Vector Machine (SVM)  
- Random Forest  
- Gradient Boosting  
- **Ensemble Model** (Soft Voting Classifier)

---

## 🧼 Data Preprocessing

- **Missing value imputation (mean):**
  - pH: 15%  
  - Sulfate: 24%  
  - Trihalomethanes: 5%
- **Feature Scaling:** StandardScaler  
- **Train-Test Split:** 80% Training, 20% Testing  
- **Feature Selection:**
  - Removed: Latitude, Longitude  
  - Retained: State (for filtering and regional analysis)

---

## 📈 Model Evaluation

**Classification Report:**

              precision    recall  f1-score   support

          no       0.98      0.93      0.96        59
         yes       0.98      1.00      0.99       214

    accuracy                           0.98       273
   macro avg       0.98      0.96      0.97       273
weighted avg       0.98      0.98      0.98       273


## 🌐 Flask Web App
A lightweight web application was developed using Flask. Users can:

Enter water sample parameters through a form.

Get an instant prediction result: Drinkable or Not Drinkable.

Download prediction result as a PDF report.

## ▶️ How to Run

Install required packages:
pip install -r requirements.txt
Run the Flask App:  python app.py
Open in browser:   http://127.0.0.1:5000

## 🏆 Results
Highest model accuracy: 98%


## 🚀 Future Scope

Integrate with IoT sensors for real-time water quality detection.

Use deep learning for advanced prediction.

Host the web app on AWS
