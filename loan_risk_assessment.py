import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(os.path.expanduser('~/Downloads/loan_application.csv'))


# cleandf = df.fillna(df.mean(), inplace=True)  # Replace missing values with mean
# lcleandf = df['loan_purpose'] = df['loan_purpose'].astype('category').cat.codes  # Encode categorical data

df['DTI'] = df['total_debt'] / df['annual_income']
df.describe()  # Get statistical insights

def risk_category(score):
    if score > 750:
        return "Low Risk"
    elif 600 <= score <= 750:
        return "Medium Risk"
    else:
        return "High Risk"

df['risk_category'] = df['credit_score'].apply(risk_category)
df.to_csv(os.path.expanduser('~/Downloads/loan_application_processed.csv'))

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X = df[['credit_score', 'DTI', 'loan_amount']]
y = df['default_flag']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

sns.boxplot(x=df['risk_category'], y=df['loan_amount'])
plt.show()