# src/data_repair.py
import pandas as pd
import os

# Ensure directory exists
os.makedirs("data/processed", exist_ok=True)

# Load raw data
df = pd.read_csv("data/raw/input.csv")

# Repair logic (simple but valid)
df = df.fillna(df.mean(numeric_only=True))

# 🚨 THIS LINE IS CRITICAL
df.to_csv("data/processed/cleaned_data.csv", index=False)

print("Cleaned dataset saved at data/processed/cleaned_data.csv")