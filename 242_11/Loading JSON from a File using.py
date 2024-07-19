
import json

# Open the JSON file
with open('./example Json/example1.json', 'r') as file:
    # Parse JSON data
    data = json.load(file)

# Accessing data
print(data['name'])  # Output: John Doe
print(data['age'])   # Output: 30
print(data['isStudent'])  # Output: False
