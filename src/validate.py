# src/validate.py
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

model = joblib.load("models/model.pkl")

X = pd.read_csv("data/processed/X_temp.csv")
y = pd.read_csv("data/processed/y_temp.csv")

# Split temp data into validation & test
X_val, X_test = X.iloc[:len(X)//2], X.iloc[len(X)//2:]
y_val, y_test = y.iloc[:len(y)//2], y.iloc[len(y)//2:]

y_pred = model.predict(X_val)
val_accuracy = accuracy_score(y_val, y_pred)

print(f"Validation Accuracy: {val_accuracy}")

# Save test data for final evaluation
X_test.to_csv("data/processed/X_test.csv", index=False)
y_test.to_csv("data/processed/y_test.csv", index=False)

# Optional quality gate
if val_accuracy < 0.5:
    raise Exception("Validation failed: accuracy below threshold")