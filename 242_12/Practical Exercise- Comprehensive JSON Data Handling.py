import json

def load_json_from_string():
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
    return json.loads(json_string)

def load_json_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def access_and_modify_json(data):
    # Accessing data
    name = data['name']
    courses = data['courses']
    city = data['address']['city']
    
    print(f"Name: {name}")
    print(f"Courses: {courses}")
    print(f"City: {city}")
    
    # Modifying data
    data['name'] = "Jane Doe"
    data['graduationYear'] = 2022
    del data['isStudent']

    return data

def generate_json_string(data):
    return json.dumps(data, indent=4)

def write_json_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def handle_complex_json(data):
    # Accessing nested data
    company_name = data['company']['name']
    employee_skills = data['employees'][0]['skills']
    
    print(f"Company Name: {company_name}")
    print(f"First Employee's Skills: {employee_skills}")
    
    # Modifying nested data
    data['employees'][1]['age'] = 26

    return data

def main():
    # Load JSON from string
    data_from_string = load_json_from_string()
    print("Loaded JSON from string:")
    print(generate_json_string(data_from_string))

    # Load JSON from file
    file_path = 'data.json'  # Ensure this file exists with valid JSON data
    data_from_file = load_json_from_file(file_path)
    print("\nLoaded JSON from file:")
    print(generate_json_string(data_from_file))

    # Access and modify JSON data
    modified_data = access_and_modify_json(data_from_file)
    print("\nModified JSON data:")
    print(generate_json_string(modified_data))

    # Write modified JSON to a new file
    output_file_path = 'modified_data.json'
    write_json_to_file(modified_data, output_file_path)
    print(f"\nModified JSON data written to {output_file_path}")

    # Handling complex JSON structure
    complex_json_string = '''
    {
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
      ],
      "company": {
        "name": "Tech Solutions",
        "location": "Silicon Valley"
      }
    }
    '''
    complex_data = json.loads(complex_json_string)
    handled_complex_data = handle_complex_json(complex_data)
    print("\nHandled complex JSON data:")
    print(generate_json_string(handled_complex_data))

if __name__ == "__main__":
    main()
