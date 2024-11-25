import pandas as pd
# Load the dataset
df = pd.read_csv('./data/sales_data_sample.csv')
# Clean the data
df = df.dropna()  # Handle missing data by dropping rows with missing values
df = df.drop_duplicates()  # Remove duplicate records
# Analyze the data
mean_revenue = df['TotalRevenue'].mean()
median_revenue = df['TotalRevenue'].median()
mode_revenue = df['TotalRevenue'].mode()[0]
# Group and aggregate the data
category_revenue = df.groupby('Category')['TotalRevenue'].mean()

# Visualize the data
category_revenue.plot(kind='bar', title='Average Revenue by Category')
# Display results
print(f"Mean Revenue: {mean_revenue}")
print(f"Median Revenue: {median_revenue}")
print(f"Mode Revenue: {mode_revenue}")
print("Average Revenue by Category:")
print(category_revenue)
