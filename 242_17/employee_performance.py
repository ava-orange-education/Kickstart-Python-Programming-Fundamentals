import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv('./data/employee_performance_sample.csv')
# Clean the data
df = df.dropna()  # Handle missing data
df = df.drop_duplicates()  # Remove duplicates

# Analyze the data
average_projects = df['ProjectsCompleted'].mean()
average_performance = df['PerformanceScore'].mean()
# Group and aggregate the data
department_performance = df.groupby('Department').agg({
    'HoursWorked': 'sum',
    'ProjectsCompleted': 'sum',
    'PerformanceScore': 'mean'
})
# Visualize the data
department_performance['PerformanceScore'].plot(kind='bar', title='Average Performance Score by Department')
plt.scatter(df['HoursWorked'], df['PerformanceScore'])
plt.title('Performance Score vs Hours Worked')
plt.xlabel('Hours Worked')
plt.ylabel('Performance Score')
plt.show()

# Display results
print(f"Average Projects Completed: {average_projects}")
print(f"Average Performance Score: {average_performance}")
print("Department Performance Summary:")
print(department_performance)
