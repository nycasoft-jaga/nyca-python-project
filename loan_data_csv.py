import pandas as pd
import numpy as np
from scipy.special import expit  # Logistic sigmoid function

# Set seed for reproducibility
np.random.seed(42)

# Number of records
n = 1000

# Generate credit_score (normally distributed around 650)
mean_credit = 650
std_credit = 100
credit_score = np.random.normal(mean_credit, std_credit, n)
credit_score = np.clip(credit_score, 300, 850).astype(int)

# Generate income (right-skewed using log-normal distribution)
income = (np.random.lognormal(mean=10, sigma=0.7, size=n) * 1000).astype(int)
income = np.clip(income, 20000, 150000)

# Generate loan_amount (random between $1k-$100k)
loan_amount = np.random.randint(1000, 100001, n)

# Generate loan_term (more short-term loans)
loan_term = np.random.choice(
    np.concatenate([np.arange(1, 6), np.arange(10, 31, 5)]),
    size=n
)

# Generate interest_rate (base rate + credit-based adjustment)
base_rate = 3.0
rate_adjustment = (850 - credit_score) * 0.02
interest_rate = base_rate + rate_adjustment + np.random.normal(0, 0.5, n)
interest_rate = np.round(np.clip(interest_rate, 3.0, 20.0), 1)

# Generate default probability using logistic function
# Higher risk factors: low credit, high loan/income ratio, high interest rate, long term
loan_to_income = loan_amount / income
z = (-0.02 * credit_score + 
      3.5 * loan_to_income + 
      0.2 * interest_rate + 
      0.05 * loan_term + 
      np.random.normal(0, 1, n) - 5)

default_prob = expit(z)  # Apply sigmoid
default = np.random.binomial(1, default_prob)  # Binary default outcome

# Create DataFrame
df = pd.DataFrame({
    'credit_score': credit_score,
    'income': income,
    'loan_amount': loan_amount,
    'loan_term': loan_term,
    'interest_rate': interest_rate,
    'default': default
})

# Save to CSV
df.to_csv('loan_data.csv', index=False)

# Verify feature-target relationship
print(f"Default rate: {df['default'].mean():.2%}")