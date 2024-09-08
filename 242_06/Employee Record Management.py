# List to store employee tuples 
employees = [] 
# Function to add employee details 
def add_employee(id, name, position, department): 
    employee = (id, name, position, department) 
    employees.append(employee) 
# Function to display employee information 
def display_employee(emp_id): 
    for employee in employees: 
        if employee[0] == emp_id: 
            _, name, position, department = employee 
            print(f"Employee Name: {name}") 
            print(f"Position: {position}") 
            print(f"Department: {department}") 
            break 
    else: 
        print("Employee not found.") 
# Adding employee details 
add_employee(1, "John Doe", "Software Developer", "Technology") 
add_employee(2, "Jane Smith", "Project Manager", "Marketing") 
# Displaying employee details 
display_employee(1) 
