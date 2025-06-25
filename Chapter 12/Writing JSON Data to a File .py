import json

# Python dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "isStudent": False,
    "courses": ["Python", "Data Science"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    }
}

# Write JSON data to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
