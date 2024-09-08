from collections import namedtuple 
# Creating a named tuple class 
Employee = namedtuple('Employee', ['name', 'department', 'position']) 
# Creating an instance of a named tuple 
emp = Employee(name="Jane Smith", department="Marketing", position="Manager") 
# Accessing elements 
print(emp.name) # Outputs: Jane Smith
