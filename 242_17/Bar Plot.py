import pandas as pd
import matplotlib.pyplot as plt 
# Assuming df is your DataFrame
df = pd.read_csv('./Practical Exercise-Working with DataFrames/data.csv')
grouped_data = df.groupby('Department')['Salary'].mean()
# Bar plot of average salary by department
grouped_data.plot(kind='bar', title='Average Salary by Department')
plt.xlabel('Department')  # Label the x-axis
plt.ylabel('Average Salary')  # Label the y-axis
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Display the plot