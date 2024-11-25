import pandas as pd
# Create a dictionary of data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
# Display the DataFrame
print(df)
