import pandas as pd
# Create a dictionary of employee data
data = {
    'Name': ['John', 'Jane', 'Emily', 'Michael'],
    'Age': [28, 34, 22, 45],
    'Department': ['HR', 'Finance', 'IT', 'Marketing']
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
# Display the DataFrame
print(df)


# Load the CSV file into a DataFrame
df = pd.read_csv('./Practical Exercise-Working with DataFrames/data.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Select the "Name" and "Salary" columns
selected_columns = df[['Name', 'Salary']]
print(selected_columns)

# Filter employees older than 30
older_than_30 = df[df['Age'] > 30]
print(older_than_30)

# Sort by "Salary" in descending order
sorted_df = df.sort_values(by='Salary', ascending=False)
print(sorted_df)
