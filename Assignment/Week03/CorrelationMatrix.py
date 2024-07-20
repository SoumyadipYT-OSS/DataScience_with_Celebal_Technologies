import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Calculate the correlation matrix
corr_matrix = df.corr()

print(corr_matrix)
