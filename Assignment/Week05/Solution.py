# Data Preprocessing

# 1. Import libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 2. Load dataset
df  = pd.read_csv("Assignment\\Week05\\country.csv")
print("• Main dataset")
print(df)

# 3. Data Cleaning (Handling Missing Values)
print("\n• Data cleaning")
df = df.dropna()
print(df,"\n")
df.info()

# 4. Transformation and Normalization
print("\n• Transformation and Normalization")
scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])
print(df[['Age', 'Salary']])

# 5. Label Encoding
print("\n• Encoding")
label_encoder = LabelEncoder()
df['Country'] = label_encoder.fit_transform(df["Country"])
print(df["Country"])

# 6. Feature Engineering (creating new features)
print("• Feature Engineering")
# df['new_feature'] = df['existingFeautre1'] some operation (it could be another column or numerical approach)
df1 = pd.read_csv("Assignment\\Week05\\country.csv")
df1 = df1.dropna()
df1['Bonus'] = df1['Salary'] / df1['Age'] * 100
df1['HRA'] = df1['Bonus'] * 4
df1['Net_Income'] = df1['Salary'] + df1['Bonus'] + df1['HRA']
print(df1)


# 7. Descriptive statistics
print("\n• Statistical Analysis")
print(df1.describe())

# 8. Regression Analysis
print("\n• Regression Analysis")
import statsmodels.api as sm
X = df1[['Bonus', 'HRA']]
Y = df1['Net_Income']
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
print(model._results)
