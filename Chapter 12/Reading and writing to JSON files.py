import json

# Open the JSON file
with open('data.json', 'r') as file:
    # Load JSON data from file
    data = json.load(file)

# Accessing data
print(data)

####################################

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
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)
