import pandas as pd
# Load a CSV file into a DataFrame
df = pd.read_csv('./data/customers-100.csv')
names = df['First Name']
print(names)

filtered_data = df[df['First Name'] == 'Sheryl']
print(filtered_data)

sorted_df = df.sort_values(by='Subscription Date')
print(sorted_df)
