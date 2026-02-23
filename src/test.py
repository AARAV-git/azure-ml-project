# src/test.py
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report

model = joblib.load("models/model.pkl")

X_test = pd.read_csv("data/processed/X_test.csv")
y_test = pd.read_csv("data/processed/y_test.csv")

y_pred = model.predict(X_test)

print("Test Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
