# Assignment 12 :
# Apply NumPy and Pandas to perform exploratory data analysis (EDA) 
# on a customer churn dataset by cleaning the data, handling missing values, 
# generating summary statistics, and identifying significant patterns through visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample customer churn dataset
data = {
    "CustomerID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Age": [25, 35, 45, 30, np.nan, 50, 40, 28, 60, 38],
    "MonthlyCharges": [50, 70, 90, 60, 80, 100, np.nan, 55, 95, 75],
    "Tenure": [2, 12, 24, 6, 18, 36, 10, 3, 48, 15],
    "Churn": ["Yes", "No", "No", "Yes", "No",
              "No", "Yes", "Yes", "No", "No"]
}

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the original dataset
print("Original Dataset:")
print(df)

# Display dataset information
print("\nDataset Information:")
df.info()

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numerical values with column means
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].mean()
)

# Remove duplicate rows
df = df.drop_duplicates()

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df)

# Generate summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Calculate the number of churned and retained customers
print("\nChurn Distribution:")
print(df["Churn"].value_counts())

# Calculate average monthly charges by churn status
print("\nAverage Monthly Charges by Churn:")
print(df.groupby("Churn")["MonthlyCharges"].mean())

# Visualize churn distribution
df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Visualize average monthly charges by churn status
df.groupby("Churn")["MonthlyCharges"].mean().plot(kind="bar")
plt.title("Average Monthly Charges by Churn Status")
plt.xlabel("Churn Status")
plt.ylabel("Average Monthly Charges")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Visualize tenure distribution
plt.hist(df["Tenure"], bins=5, edgecolor="black")
plt.title("Customer Tenure Distribution")
plt.xlabel("Tenure (Months)")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()
