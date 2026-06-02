import streamlit as st
import pandas as pd
import joblib

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="wide"
)

# =========================
# LOAD MODEL & DATA
# =========================

model = joblib.load("models/crop_yield_model.pkl")
df = pd.read_csv("data/crop_yield.csv")

# =========================
# HEADER
# =========================

st.title("🌾 Crop Yield Prediction System")

st.markdown("""
### Machine Learning Based Agricultural Yield Forecasting

Predict crop yield using:

- Crop Type
- State
- Season
- Rainfall
- Fertilizer Usage
- Pesticide Usage
- Area

Built using Random Forest Regression.
""")

# =========================
# METRICS
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Records", f"{len(df):,}")

with col2:
    st.metric("States", df["State"].nunique())

with col3:
    st.metric("Crops", df["Crop"].nunique())

with col4:
    st.metric("Model", "Random Forest")

st.divider()

# =========================
# DATASET INSIGHTS
# =========================

st.header("📊 Dataset Insights")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Yield Distribution")
    st.image("outputs/yield_distribution.png")

with col2:
    st.subheader("Top Crops")
    st.image("outputs/top_crops.png")

st.subheader("Top States")
st.image("outputs/top_states.png")

st.divider()

# =========================
# PREDICTION SECTION
# =========================

st.header("🌱 Predict Crop Yield")

col1, col2 = st.columns(2)

with col1:

    crop = st.selectbox(
        "Select Crop",
        sorted(df["Crop"].unique())
    )

    season = st.selectbox(
        "Select Season",
        sorted(df["Season"].unique())
    )

    state = st.selectbox(
        "Select State",
        sorted(df["State"].unique())
    )

    crop_year = st.number_input(
        "Crop Year",
        min_value=1997,
        max_value=2035,
        value=2020
    )

with col2:

    area = st.number_input(
        "Area",
        min_value=0.0,
        value=5000.0
    )

    rainfall = st.number_input(
        "Annual Rainfall",
        min_value=0.0,
        value=1500.0
    )

    fertilizer = st.number_input(
        "Fertilizer",
        min_value=0.0,
        value=1000.0
    )

    pesticide = st.number_input(
        "Pesticide",
        min_value=0.0,
        value=200.0
    )

# =========================
# PREDICTION
# =========================

if st.button("🚀 Predict Yield"):

    sample = pd.DataFrame({
        "Crop": [crop],
        "Crop_Year": [crop_year],
        "Season": [season],
        "State": [state],
        "Area": [area],
        "Annual_Rainfall": [rainfall],
        "Fertilizer": [fertilizer],
        "Pesticide": [pesticide]
    })

    prediction = model.predict(sample)

    st.success(
        f"🌾 Predicted Crop Yield: {prediction[0]:.2f}"
    )

st.divider()

# =========================
# PROJECT HIGHLIGHTS
# =========================

st.markdown("""
## 📌 Project Highlights

✅ Random Forest Regression

✅ Agricultural Analytics

✅ Crop Yield Forecasting

✅ State-wise Analysis

✅ Crop-wise Insights

✅ Interactive Dashboard

✅ Streamlit Deployment Ready
""")