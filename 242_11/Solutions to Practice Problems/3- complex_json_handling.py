import json

def complex_json_handling():
    # Complex JSON string
    json_string = '''
    {
        "company": {
            "name": "Tech Solutions",
            "employees": [
                {
                    "name": "John Doe",
                    "age": 30,
                    "skills": ["Python", "Data Analysis"]
                },
                {
                    "name": "Jane Smith",
                    "age": 25,
                    "skills": ["JavaScript", "Web Development"]
                }
            ]
        }
    }
    '''
    
    # Parse JSON string
    data = json.loads(json_string)
    print("Original JSON data:", data)
    
    # Access and modify nested data
    data['company']['employees'][1]['age'] = 26
    new_skill = "Project Management"
    data['company']['employees'][1]['skills'].append(new_skill)
    
    # Convert to JSON string
    modified_json_string = json.dumps(data, indent=4)
    print("Modified JSON data:", modified_json_string)

# Execute the function if the script is run directly
if __name__ == "__main__":
    complex_json_handling()
