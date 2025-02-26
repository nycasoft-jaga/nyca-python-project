# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Step 1: Simulating Data Collection (Synthetic Dataset)
np.random.seed(42)
num_samples = 1000

df = pd.DataFrame({
    "Credit Score": np.random.normal(loc=700, scale=50, size=num_samples).astype(int),  # Mean 700, Std 50
    "Income": np.random.normal(loc=50000, scale=15000, size=num_samples).astype(int),  # Mean 50k, Std 15k
    "Debt-to-Income Ratio": np.random.uniform(0.1, 0.5, size=num_samples),  # Random between 10% to 50%
    "Existing Loans": np.random.randint(0, 5, size=num_samples),  # 0 to 4 existing loans
    "Loan Amount Requested": np.random.randint(5000, 50000, size=num_samples),  # Loan request between 5k to 50k
    "Employment Status": np.random.choice(["Employed", "Self-Employed", "Unemployed"], size=num_samples),
    "Loan Term": np.random.choice(["12 months", "36 months", "60 months"], size=num_samples),
    "Bankruptcy History": np.random.choice([0, 1], size=num_samples, p=[0.9, 0.1]),  # 90% No, 10% Yes
    "Default": np.random.choice([0, 1], size=num_samples, p=[0.8, 0.2])  # 80% No Default, 20% Default
})

# Introduce some missing values for testing
df.loc[np.random.choice(df.index, size=50, replace=False), "Income"] = np.nan
df.loc[np.random.choice(df.index, size=30, replace=False), "Employment Status"] = np.nan

# Step 2: Handling Missing Values
df["Income"].fillna(df["Income"].median(), inplace=True)  # Fill missing income with median
df["Employment Status"].fillna(df["Employment Status"].mode()[0], inplace=True)  # Fill categorical missing with mode

# Step 3: Scaling Continuous Features (Min-Max Scaling)
scaler = MinMaxScaler()
df[["Credit Score", "Income", "Debt-to-Income Ratio", "Loan Amount Requested"]] = scaler.fit_transform(
    df[["Credit Score", "Income", "Debt-to-Income Ratio", "Loan Amount Requested"]])

# Step 4: Encoding Categorical Variables
df = pd.get_dummies(df, columns=["Employment Status", "Loan Term"], drop_first=True)  # One-hot encoding
label_encoder = LabelEncoder()
df["Bankruptcy History"] = label_encoder.fit_transform(df["Bankruptcy History"])  # Label encoding

# Step 5: Feature Engineering - Creating a "Risk Score"
df["Risk Score"] = df["Credit Score"] / (df["Debt-to-Income Ratio"] + 0.01)  # Avoid division by zero

# Step 6: Splitting Data for Training & Testing
X = df.drop(columns=["Default"])  # Features
y = df["Default"]  # Target variable (1 = Default, 0 = No Default)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Display Processed Data Information
print("Processed Dataset Sample:")
print(df)

# Step 8: Visualizing the Distribution of Credit Scores
sns.histplot(df["Credit Score"], bins=30, kde=True, color="blue")
plt.title("Distribution of Credit Scores (Normalized)")
plt.xlabel("Credit Score (Scaled)")
plt.ylabel("Density")
plt.show()