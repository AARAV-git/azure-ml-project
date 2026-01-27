# from azureml.core import Workspace

# ws = Workspace.from_config()
# print("CONNECTED TO:", ws.name)
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# -----------------------------
# 1. Generate Random Dataset
# -----------------------------
np.random.seed(42)

X = np.random.rand(1000, 10)      # 1000 samples, 10 features
y = np.random.randint(0, 2, 1000) # Binary labels (0/1)

# -----------------------------
# 2. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 3. Train Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# 4. Test Model
# -----------------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# -----------------------------
# 5. Save Model
# -----------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/random_forest_model.pkl")

print("Model saved in models/random_forest_model.pkl")
