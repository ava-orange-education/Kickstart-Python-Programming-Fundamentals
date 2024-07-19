import json

def basic_json_parsing():
    # JSON string
    json_string = '{"name": "John Doe", "age": 30, "isStudent": false}'
    
    # Parse JSON string
    data = json.loads(json_string)
    print("Original JSON data:", data)
    
    # Modify JSON data
    data['name'] = "Jane Doe"
    data['age'] = 25
    data['graduationYear'] = 2022
    
    # Convert to JSON string
    modified_json_string = json.dumps(data, indent=4)
    print("Modified JSON data:", modified_json_string)

# Execute the function if the script is run directly
if __name__ == "__main__":
    basic_json_parsing()
