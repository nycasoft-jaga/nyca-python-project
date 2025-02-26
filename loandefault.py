import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Generating synthetic data for credit scores
np.random.seed(42)
credit_scores = np.random.normal(loc=700, scale=50, size=1000)  # Mean 700, Std 50

# Visualizing the normal distribution
sns.histplot(credit_scores, bins=30, kde=True, stat="density", color='blue')
x = np.linspace(550, 850, 100)
plt.plot(x, norm.pdf(x, np.mean(credit_scores), np.std(credit_scores)), 'r-', lw=2)
plt.title("Normal Distribution of Credit Scores")
plt.xlabel("Credit Score")
plt.ylabel("Density")
# plt.show()

import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample dataset
data = {
    'credit_score': np.random.normal(700, 50, 1000),  # Mean 700, Std 50
    'income': np.random.normal(50000, 15000, 1000),  # Mean 50K, Std 15K
    'loan_amount': np.random.normal(20000, 5000, 1000)  # Mean 20K, Std 5K
}
df = pd.DataFrame(data)

# Standardizing data
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Display first few rows
print(df_scaled.head())
