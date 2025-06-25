import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset into a DataFrame
df = pd.read_csv('./data/sample_data_100_entries.csv')

# Calculate and display statistics for 'Sales'
print("Mean Sales:", df['Sales'].mean())
print("Median Sales:", df['Sales'].median())
print("Mode Sales:", df['Sales'].mode()[0])
print("Standard Deviation of Sales:", df['Sales'].std())

# Group by 'Category' and calculate the mean sales for each category
category_sales = df.groupby('Category')['Sales'].mean()
print("\nAverage Sales by Category:\n", category_sales)

# Group by 'Category' and aggregate multiple statistics
aggregated_data = df.groupby('Category').agg({
    'Sales': ['mean', 'sum'],
    'Quantity': 'sum'
})
print("\nAggregated Data by Category:\n", aggregated_data)

# Bar plot: Average Sales by Category
category_sales.plot(kind='bar', title='Average Sales by Category')
plt.xlabel('Category')
plt.ylabel('Average Sales')
plt.tight_layout()
plt.show()

# Line plot: Sales Over Time
df.plot(x='Month', y='Sales', kind='line', title='Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# Histogram: Sales Distribution
df['Sales'].plot(kind='hist', title='Sales Distribution', bins=10)
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter plot: Sales vs. Advertising Spend
df.plot(kind='scatter', x='AdvertisingSpend', y='Sales', title='Sales vs. Advertising Spend')
plt.xlabel('Advertising Spend')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
