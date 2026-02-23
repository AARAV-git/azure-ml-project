# src/train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_data.csv")

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "models/model.pkl")

# Save remaining data for validation/testing
X_temp.to_csv("data/processed/X_temp.csv", index=False)
y_temp.to_csv("data/processed/y_temp.csv", index=False)