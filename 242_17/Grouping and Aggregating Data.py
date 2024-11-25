import pandas as pd
# Assuming df is your DataFrame
df = pd.read_csv('./Practical Exercise-Working with DataFrames/data.csv')
# Group by a column (e.g., 'Department') and calculate the mean of another column (e.g., 'Salary')
grouped_data = df.groupby('Department')['Salary'].mean()
print(grouped_data)
# You can also perform multiple aggregations
aggregated_data = df.groupby('Department').agg({
    'Salary': ['mean', 'max', 'min']
})
print(aggregated_data)
