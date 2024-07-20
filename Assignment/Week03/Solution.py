import pandas as pd


#1. Uploading the dataset
download_df_dataset = pd.read_csv("C:\\Users\\HP\\Desktop\\AEP_hourly.csv")


#2. Find the shape(number of rows (data points), columns(features))
num_rows, num_columns = download_df_dataset.shape
print(f"Number of rows (data points): {num_rows} samples")
print(f"Number of columns (features): {num_columns} features") 


#3. Check for Null Values
null_counts = download_df_dataset.isnull().sum()
print("Null counts per column: ")
print(null_counts)


#4. Data Types of Columns
data_types = download_df_dataset.dtypes
print("Data types per column: ")
print(data_types)


#5. Find the statistical information for each numerical column
numerical_stats = download_df_dataset.describe()
print("Statistical information for numerical columns: ")
print(numerical_stats)


#6. Convert Categorical Columns to Numerical (If it possible)
categorical_columns = download_df_dataset.select_dtypes(include=['datetime']).columns

if len(categorical_columns) > 0:
    download_df_dataset = pd.get_dummies(download_df_dataset, columns=categorical_columns, drop_first=True)
    print("Converted categorical columns to numerical using one-hot encoding.")
else:
    print("No categorical columns found in the dataset.")




#7. Find the corrrelation matrix
# See the "CorrelatioMatrix.py" solution




#8. Data Visualization using matplotlib
import matplotlib.pyplot as plt
import numpy as np

download_df_dataset['Datetime'] = pd.to_datetime(download_df_dataset['Datetime'])

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(8, 6))
plt.plot(download_df_dataset['Datetime'], download_df_dataset['AEP_MW'], 
    color='#007acc', 
    label='Energy Consumption', 
linewidth=0.5)

plt.xlabel('Date and Time (Yearly)')
plt.ylabel('Energy Consumption (MW)')
plt.title('Hourly Energy Consumption over time')
plt.grid(True, alpha=0.5)
plt.legend()
plt.show()
