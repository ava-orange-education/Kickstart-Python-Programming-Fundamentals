import sqlite3
from pymongo import MongoClient

# SQLite setup for storing student information
sqlite_connection = sqlite3.connect('students.db')
sqlite_cursor = sqlite_connection.cursor()
sqlite_cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        course TEXT NOT NULL
    )
''')

# MongoDB setup for storing grades
mongo_client = MongoClient('localhost', 27017)
grades_db = mongo_client['student_grades']
grades_collection = grades_db['grades']

# Function to add a student
def add_student(name, course):
    sqlite_cursor.execute('''
        INSERT INTO students (name, course)
        VALUES (?, ?)
    ''', (name, course))
    sqlite_connection.commit()

# Function to add a grade for a student
def add_grade(student_id, course, grade):
    grade_record = {
        "student_id": student_id,
        "course": course,
        "grade": grade
    }
    grades_collection.insert_one(grade_record)

# Function to retrieve a student's grades
def get_student_grades(student_id):
    return grades_collection.find({"student_id": student_id})

# Example usage
add_student("Alice Johnson", "Math 101")
add_grade(1, "Math 101", 95)
add_grade(1, "Math 101", 87)
grades = get_student_grades(1)
for grade in grades:
    print(grade)

# Close connections
sqlite_connection.close()
mongo_client.close()
