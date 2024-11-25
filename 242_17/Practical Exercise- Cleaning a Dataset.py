import pandas as pd
# Load the dataset into a DataFrame
df = pd.read_csv('./data/DataCleasing.csv')

# Identify missing values
print("Missing values in each column:\n", df.isnull().sum())
# Fill missing values with the mean (or drop rows with missing values)
df = df.fillna(df['Salary'].mean())

# Identify and remove duplicates
df = df.drop_duplicates()

# Convert 'Salary' to integer and 'HireDate' to datetime
df['Salary'] = df['Salary'].astype(int)
df['HireDate'] = pd.to_datetime(df['HireDate'])

# Rename columns and set 'EmployeeID' as the index
df = df.rename(columns={'EmpID': 'EmployeeID', 'Dept': 'Department'})
df = df.set_index('EmployeeID')
# Reorder columns
df = df[['Name', 'Department', 'Salary', 'HireDate']]
print(df)

