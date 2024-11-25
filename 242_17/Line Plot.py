import pandas as pd
import matplotlib.pyplot as plt 
# Assuming df is your DataFrame
df = pd.read_csv('./Practical Exercise-Working with DataFrames/data.csv')
df.plot(x='Date', y='Salary', kind='line', title='Salary Over Time')
plt.xlabel('Date')  # Label the x-axis
plt.ylabel('Salary')  # Label the y-axis
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Display the plot