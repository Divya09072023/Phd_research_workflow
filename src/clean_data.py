import pandas as pd
import os

# Step 1: Define file paths
input_path = "C:\Phd_research_workflow\data\sample_data.csv"
output_path = 'C:\Phd_research_workflow\data\cleaned_data.csv'

# Step 2: Load the dataset
try:
    df = pd.read_csv(input_path)
    print("✅ Data loaded successfully\n")
except FileNotFoundError:
    print("❌ File not found. Check the path:", input_path)
    exit()

# Step 3: Show missing values before cleaning
print("Missing values BEFORE cleaning:\n")
print(df.isnull().sum())

# Step 4: Fill missing numeric values with 0
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_columns] = df[numeric_columns].fillna(0)

# Step 5: Show missing values after cleaning
print("\nMissing values AFTER cleaning:\n")
print(df.isnull().sum())

# Step 6: Save cleaned dataset
df.to_csv(output_path, index=False)

print("\n✅ Cleaned data saved successfully at:", output_path)