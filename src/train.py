# src/train.py
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

path = "data/processed/cleaned_data.csv"

if not os.path.exists(path):
    raise FileNotFoundError(f"❌ Required file not found: {path}. Run data_repair.py first.")

df = pd.read_csv(path)

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")

X_temp.to_csv("data/processed/X_temp.csv", index=False)
y_temp.to_csv("data/processed/y_temp.csv", index=False)

print("✅ Model training completed successfully")