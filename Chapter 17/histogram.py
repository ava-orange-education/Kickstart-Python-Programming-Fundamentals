import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your DataFrame
df = pd.read_csv('./Practical Exercise-Working with DataFrames/data.csv')

# Histogram of salaries
df['Salary'].plot(kind='hist', title='Salary Distribution')
plt.xlabel('Salary')  # Label the x-axis
plt.ylabel('Frequency')  # Label the y-axis
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Display the histogram