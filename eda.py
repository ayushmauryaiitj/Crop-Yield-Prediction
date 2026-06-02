import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/crop_yield.csv")

# Top 10 Crops by Yield
top_crops = (
    df.groupby("Crop")["Yield"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
sns.barplot(x=top_crops.values, y=top_crops.index)
plt.title("Top 10 Crops by Average Yield")
plt.tight_layout()
plt.savefig("outputs/top_crops.png")
plt.close()

# Top 10 States by Yield
top_states = (
    df.groupby("State")["Yield"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
sns.barplot(x=top_states.values, y=top_states.index)
plt.title("Top 10 States by Average Yield")
plt.tight_layout()
plt.savefig("outputs/top_states.png")
plt.close()

# Yield Distribution
plt.figure(figsize=(10,5))
sns.histplot(df["Yield"], bins=50, kde=True)
plt.title("Yield Distribution")
plt.tight_layout()
plt.savefig("outputs/yield_distribution.png")
plt.close()

print("Graphs Generated Successfully!")