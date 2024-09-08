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

# Convert to JSON string
json_string = json.dumps(data, indent=4)
print(json_string)
