import numpy as np
import pandas as pd
import math
from numpy.linalg import eig
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score

# Load dataset (assuming a CSV with relevant financial features)
df = pd.read_csv("loan_data.csv")

# Select relevant features
features = ['credit_score', 'income', 'loan_amount', 'loan_term', 'interest_rate']
X = df[features].values
y = df['default'].values  # Binary target variable (1 for default, 0 otherwise)

# Normalize data (Assuming normal distribution)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Eigen vectors for dimensionality reduction
cov_matrix = np.cov(X_scaled.T)
eigen_values, eigen_vectors = eig(cov_matrix)

# Reduce dimensions using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict probability of default
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Calculate probability using sigmoid function
sigmoid = lambda x: 1 / (1 + math.exp(-x))
probabilities = [sigmoid(np.dot(model.coef_, x) + model.intercept_) for x in X_test]

# Print results
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print(f"Sample Default Probabilities: {probabilities[:10]}")