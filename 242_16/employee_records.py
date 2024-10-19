import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('employee_records.db')
cursor = connection.cursor()

# Create a table for storing employee records
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary REAL
    )
''')

# Function to add a new employee
def add_employee(name, department, salary):
    cursor.execute('''
        INSERT INTO employees (name, department, salary)
        VALUES (?, ?, ?)
    ''', (name, department, salary))
    connection.commit()

# Function to retrieve employee details by department
def get_employees_by_department(department):
    cursor.execute('''
        SELECT * FROM employees WHERE department = ?
    ''', (department,))
    return cursor.fetchall()

# Function to update an employee's department or salary
def update_employee(employee_id, department=None, salary=None):
    if department:
        cursor.execute('''
            UPDATE employees SET department = ? WHERE employee_id = ?
        ''', (department, employee_id))
    if salary:
        cursor.execute('''
            UPDATE employees SET salary = ? WHERE employee_id = ?
        ''', (salary, employee_id))
    connection.commit()

# Function to delete an employee record
def delete_employee(employee_id):
    cursor.execute('''
        DELETE FROM employees WHERE employee_id = ?
    ''', (employee_id,))
    connection.commit()

# Example usage
add_employee('John Doe', 'Engineering', 75000)
add_employee('Jane Smith', 'Marketing', 65000)
print("Employees in Engineering:", get_employees_by_department('Engineering'))
update_employee(1, salary=80000)
delete_employee(2)
print("All Employees:", get_employees_by_department('Engineering'))

# Close the connection
connection.close()
