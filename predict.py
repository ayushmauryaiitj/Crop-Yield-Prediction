import pandas as pd
import joblib

model = joblib.load("models/crop_yield_model.pkl")

sample = pd.DataFrame({
    "Crop": ["Rice"],
    "Crop_Year": [2020],
    "Season": ["Kharif"],
    "State": ["Assam"],
    "Area": [5000],
    "Annual_Rainfall": [1800],
    "Fertilizer": [1200],
    "Pesticide": [200]
})

prediction = model.predict(sample)

print("\nPredicted Crop Yield:")
print(round(prediction[0], 2))