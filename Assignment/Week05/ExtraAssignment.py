# import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


# Load your dataset
df = pd.read_csv('Assignment\\Week05\\PerCapita.csv')

# Find the number of rows and columns
rows, columns = df.shape
print(f"Number of Rows: {rows}")
print(f"Number of Columns: {columns}")

# View the top few rows of the dataset
print(df.head())

# view the data types of each column
print(df.dtypes)

print("\n• Statistical Overview")
print(df.describe())


print("• Fill NaN values of 'age' column with its mean")
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df['Age'])


print("\n• Fill NaN of 'major/Minor' column with its mode")
mode_value = df['Major/Minor'].mode()[0]
df['Major/Minor'] = df['Major/Minor'].fillna(mode_value)
print(df['Major/Minor'])


# Fill NaN columns with zero
print("• Fill NaN columns with zero")
if 'Major/Minor' in df.columns:
    label_encoder = LabelEncoder()
    df['Major/Minor'] = label_encoder.fit_transform(df["Major/Minor"])
else:
    print("Column 'Major/Minor' not found in the dataset.")
df = df.fillna(0)

# Replace categorical values with numerical values
print("\n• Replace categorical column")
if 'Major/Minor' in df.columns:
    label_encoder = LabelEncoder()
    df['Major/Minor'] = label_encoder.fit_transform(df['Major/Minor'])
else:
    print("Column 'Major/Minor' not found in the dataset.")

# Apply onehot encoding
print("\n• Apply onehot encoding")
df = pd.get_dummies(df, columns=['Country'])


# Split the dataset 60% trainning and 40% test
print("\n• Trainning and Testing")
train_df, test_df = train_test_split(df, test_size=0.4, random_state=42)
print(f"Training set shape: {train_df}")
print(f"Testing set shape: {test_df}")

# Split the test dataset into test (50%) and validation (50%) sets
print("\n• Validating")
test_df, validation_df = train_test_split(test_df, test_size=0.5, random_state=42)
print(f"Test set shape: {test_df}")
print(f"Validation set shape: {validation_df}")

