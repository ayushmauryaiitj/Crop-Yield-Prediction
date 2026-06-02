# 🌾 Crop Yield Prediction System

A Machine Learning based web application that predicts agricultural crop yield using environmental and farming-related factors such as crop type, state, rainfall, fertilizer usage, pesticide usage, area, season, and year.

## 🚀 Live Demo

🔗 https://crop-yield-prediction-in.streamlit.app/

---

## 📌 Project Overview

Crop yield prediction is an important agricultural problem that helps farmers, researchers, and policymakers estimate future production based on historical and environmental data.

This project uses a Random Forest Regression model trained on Indian agricultural crop yield data to predict crop production efficiency.

---

## 🎯 Features

✅ Interactive Streamlit Web Application

✅ Machine Learning Based Prediction

✅ Agricultural Dataset Analysis

✅ Crop-wise Insights

✅ State-wise Insights

✅ Yield Distribution Visualization

✅ Real-Time Crop Yield Forecasting

✅ User-Friendly Dashboard

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- Random Forest Regressor

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Web Framework

- Streamlit

---

## 📂 Project Structure

```bash
Crop-Yield-Prediction/
│
├── data/
│   └── crop_yield.csv
│
├── models/
│   └── crop_yield_model.pkl
│
├── outputs/
│   ├── yield_distribution.png
│   ├── top_crops.png
│   └── top_states.png
│
├── app.py
├── train.py
├── predict.py
├── eda.py
├── requirements.txt
└── README.md
```

---

## 📊 Input Features

The model uses the following features:

| Feature | Description |
|----------|------------|
| Crop | Crop Type |
| Crop_Year | Year of Cultivation |
| Season | Growing Season |
| State | Indian State |
| Area | Cultivated Area |
| Annual Rainfall | Annual Rainfall |
| Fertilizer | Fertilizer Usage |
| Pesticide | Pesticide Usage |

---

## 🤖 Machine Learning Model

Model Used:

**Random Forest Regressor**

Why Random Forest?

- Handles non-linear relationships effectively
- Works well with mixed numerical and categorical data
- Reduces overfitting compared to a single decision tree
- Provides strong prediction performance

---

## 📈 Model Performance

| Metric | Value |
|----------|----------|
| R² Score | 0.98 |
| MAE | 9.39 |
| RMSE | 125.88 |

The model achieved excellent prediction accuracy on the test dataset.

---

## 📊 Exploratory Data Analysis

The project includes:

### Yield Distribution

- Distribution of crop yields across records.

### Top Crops

- Highest average yielding crops.

### Top States

- States with highest average crop yield.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/ayushmauryaiitj/Crop-Yield-Prediction.git
```

Move into the project directory:

```bash
cd Crop-Yield-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train.py
```

Run the application:

```bash
streamlit run app.py
```

---

## 🌐 Deployment

The application is deployed on Streamlit Cloud.

Live Link:

https://crop-yield-prediction-in.streamlit.app/

---

## 📷 Application Preview

Features available in dashboard:

- Dataset Overview
- Yield Distribution
- Top Yielding Crops
- Top Performing States
- Real-Time Crop Yield Prediction

---

## 🔮 Future Improvements

- Weather API Integration
- Satellite Data Integration
- NDVI Based Prediction
- Deep Learning Models
- Crop Recommendation System
- Fertilizer Recommendation System
- District-Level Prediction

---

## 👨‍💻 Author

**Ayush Maurya**

Student | Machine Learning Enthusiast

GitHub:
https://github.com/ayushmauryaiitj

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share it with others

---