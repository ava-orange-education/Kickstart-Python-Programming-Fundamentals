import json

# JSON string
json_string = '''
{
  "name": "John Doe",
  "age": 30,
  "isStudent": false,
  "courses": ["Python", "Data Science"],
  "address": {
    "street": "123 Main St",
    "city": "Anytown"
  }
}
'''

# Parse JSON string
data = json.loads(json_string)

# Accessing data
name = data['name']
age = data['age']
is_student = data['isStudent']
courses = data['courses']
city = data['address']['city']

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Is Student: {is_student}")
print(f"Courses: {courses}")
print(f"City: {city}")
