import pandas as pd

# Load dataset
df = pd.read_csv("hospital_operations_data.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset size
print("\nDataset shape:")
print(df.shape)

# Column names
print("\nColumn names:")
print(df.columns.tolist())

# Data types
print("\nData types:")
print(df.dtypes)

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Basic statistics
print("\nBasic statistics:")
print(df.describe(include="all"))