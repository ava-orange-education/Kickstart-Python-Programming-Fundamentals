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

# Updating existing data
data['name'] = "Jane Doe"
data['age'] = 25

# Adding new data
data['graduationYear'] = 2022

# Removing data
del data['isStudent']

print("Updated JSON data:")
print(json.dumps(data, indent=4))
