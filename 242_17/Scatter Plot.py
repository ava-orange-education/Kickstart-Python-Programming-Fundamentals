import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your DataFrame
df = pd.read_csv('./Practical Exercise-Working with DataFrames/data.csv')

# Scatter plot of salary vs. years of experience
df.plot(kind='scatter', x='YearsExperience', y='Salary', title='Salary vs. Experience')
plt.xlabel('Years of Experience')  # Label the x-axis
plt.ylabel('Salary')  # Label the y-axis
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  # Display the scatter plot
