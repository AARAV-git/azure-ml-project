import pandas as pd
import numpy as np
import os

# Ensure folders exist
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

np.random.seed(42)
rows = 300

data = {
    "age": np.random.randint(18, 65, rows),
    "income": np.random.randint(20000, 150000, rows),
    "experience": np.random.randint(0, 40, rows),
    "credit_score": np.random.randint(300, 850, rows),
    "loan_amount": np.random.randint(5000, 500000, rows),
    "target": np.random.choice([0, 1], rows)
}

df = pd.DataFrame(data)

# Introduce missing values (to show self-healing)
df.loc[df.sample(frac=0.1).index, "income"] = None
df.loc[df.sample(frac=0.1).index, "credit_score"] = None

# Save raw data
df.to_csv("data/raw/input.csv", index=False)

# Simple cleaning (same logic as data_repair)
df = df.fillna(df.mean(numeric_only=True))

# Save cleaned data (THIS is what train.py needs)
df.to_csv("data/processed/cleaned_data.csv", index=False)

print("Dataset generated and cleaned successfully")