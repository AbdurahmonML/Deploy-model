import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

california_housing = fetch_california_housing()
X = california_housing.data
y = california_housing.target  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape)

model = LinearRegression()
model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)
model_path = "models/model.pkl"
joblib.dump(model, model_path)
