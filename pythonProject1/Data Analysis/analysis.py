import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the cleaned CSV file
df = pd.read_csv('tax_data_cleaned_v6.csv')

# Renaming columns for clarity
df.rename(columns={
    'tax_year': 'Year',
    'number_of_all_returns': 'Total Returns',
    'ny_agi_of_all_returns_in_thousands': 'Total AGI (Thousands)',
    'tax_liability_of_all_returns_in_thousands': 'Total Tax Liability (Thousands)',
    'number_of_taxable_returns': 'Taxable Returns',
    'ny_agi_of_taxable_returns_in_thousands': 'Taxable AGI (Thousands)',
    'tax_liability_of_taxable_returns_in_thousands': 'Taxable Tax Liability (Thousands)',
    'number_of_nontaxable_returns': 'Non-Taxable Returns',
    'ny_agi_of_nontaxable_returns_in_thousands': 'Non-Taxable AGI (Thousands)',
    'average_ny_agi_of_all_returns': 'Average AGI (All Returns)',
    'average_tax_of_all_returns': 'Average Tax (All Returns)',
    'average_ny_agi_of_taxable_returns': 'Average AGI (Taxable Returns)',
    'average_tax_of_taxable_returns': 'Average Tax (Taxable Returns)',
    'average_ny_agi_of_nontaxable_returns': 'Average AGI (Non-Taxable Returns)',
}, inplace=True)

# Display basic information about the DataFrame
print("DataFrame loaded successfully.")
print("Columns available in the DataFrame:")
print(df.columns)
print("Data types in the DataFrame:")
print(df.dtypes)

print("----------------")

# Show the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Summary statistics for numeric columns
print("Summary statistics for numeric columns:")
print(df.describe())

# Check for any remaining missing values
print("Missing data in the DataFrame:")
print(df.isnull().sum())

print("----------------")

# Distribution of 'Year'
plt.figure(figsize=(10, 6))
df['Year'].hist(bins=range(int(df['Year'].min()), int(df['Year'].max()) + 1))
plt.title('Distribution of Tax Years')
plt.xlabel('Year')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

print("----------------")

# Correlation matrix
# Filter only numeric columns
numeric_df = df.select_dtypes(include=[np.number])

# Compute the correlation matrix
correlation_matrix = numeric_df.corr()

# Plot Correlation Heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.xticks(rotation=45, ha='right')  # Rotate x labels for better readability
plt.yticks(rotation=0)  # Rotate y labels for better readability
plt.show()

print("----------------")

# Scatter plot example (Average AGI vs. Average Tax)
plt.figure(figsize=(10, 6))
plt.scatter(df['Average AGI (Taxable Returns)'], df['Average Tax (Taxable Returns)'], alpha=0.5)
plt.title('Average AGI vs. Average Tax for Taxable Returns')
plt.xlabel('Average AGI (Taxable Returns)')
plt.ylabel('Average Tax (Taxable Returns)')
plt.grid(True)
plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(df['Taxable AGI (Thousands)'], df['Non-Taxable AGI (Thousands)'], alpha=0.5)
plt.title('Taxable AGI vs Non-Taxable AGI')
plt.xlabel('Taxable AGI (Thousands)')
plt.ylabel('Non-Taxable AGI (Thousands)')
plt.grid(True)
plt.show()
