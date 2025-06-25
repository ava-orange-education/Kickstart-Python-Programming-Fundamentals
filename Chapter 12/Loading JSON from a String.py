import json

# JSON string
json_string = '{"name": "John Doe", "age": 30, "isStudent": false}'

# Parse JSON string
data = json.loads(json_string)

# Accessing data
print(data['name'])  # Output: John Doe
print(data['age'])   # Output: 30
print(data['isStudent'])  # Output: False
