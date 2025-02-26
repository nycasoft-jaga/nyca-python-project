# Loan Default Probability Prediction

This repository contains a Python script that predicts the probability of loan default using machine learning techniques.<br/>
The model utilizes logistic regression with principal component analysis (PCA) for dimensionality reduction.

## Features

- Loads financial data from `loan_data.csv`
- Normalizes selected features using `StandardScaler`
- Performs PCA for dimensionality reduction
- Trains a logistic regression model
- Predicts loan default probability
- Outputs model accuracy and sample default probabilities

## Requirements

Ensure you have the following Python libraries installed:

    pip install numpy pandas scikit-learn

## **Usage**

1. Place your dataset (`loan_data.csv`) in the same directory as the script.
2. Run the script:

     ```bash
     python loandefault_probability.py

## Dataset Format
The dataset should be a CSV file (`loan_data.csv`) with the following columns:

| credit_score | income | loan_amount | loan_term | interest_rate | default |
|-------------|--------|-------------|------------|--------------|---------|
| 720         | 50000  | 20000       | 60         | 5.5          | 0       |
| 650         | 40000  | 25000       | 48         | 7.2          | 1       |
| ...         | ...    | ...         | ...        | ...          | ...     |

- `default`: Binary column (1 = default, 0 = no default)

## Model Explanation
**Feature Selection:** Uses credit_score, income, loan_amount, loan_term, and interest_rate.<br/>
**Normalization:** Standardizes features for better performance.<br/>
**Dimensionality Reduction:** Uses PCA to reduce features to two principal components.<br/>
**Logistic Regression:** Predicts the probability of loan default.<br/>
**Evaluation:** Prints model accuracy and sample probabilities.

## License
This project is open-source and available.

