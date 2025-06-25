import pandas as pd
# Assuming df is your DataFrame
# Calculate mean of a column
df = pd.read_csv('./Practical Exercise-Working with DataFrames/data.csv')
mean_value = df['Salary'].mean()
print(f"Mean Salary: {mean_value}")
# Calculate median of a column
median_value = df['Salary'].median()
print(f"Median Salary: {median_value}")
# Calculate mode of a column
mode_value = df['Salary'].mode()[0]  # [0] to get the first mode
print(f"Mode Salary: {mode_value}")
# Calculate standard deviation of a column
std_dev = df['Salary'].std()
print(f"Standard Deviation of Salary: {std_dev}")
