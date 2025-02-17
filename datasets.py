import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, accuracy_score

df = pd.read_csv('/Users/jagadeeshmuvva/Downloads/StudentPerformanceFactors.csv')

df.shape
df.info()
df.describe()
df.isnull().sum()

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.show()

sns.histplot(df['scores'], kde=True)
plt.show()

sns.boxplot(x='gender', y='scores', data=df)
plt.show()

sns.scatterplot(x='study_time', y='scores', data=df)
plt.show()

df.fillna(df.mean(), inplace=True)
df = pd.get_dummies(df, drop_first=True)

X = df[['study_time', 'parental_education', 'gender_Male']]  # Example features
y = df['scores']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')