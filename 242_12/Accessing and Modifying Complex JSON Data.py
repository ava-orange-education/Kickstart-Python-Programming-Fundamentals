import json

# JSON string
json_string = '''
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

# Parse JSON string
data = json.loads(json_string)

# Accessing nested data
company_name = data['company']['name']
employee_skills = data['employees'][0]['skills']

print(f"Company Name: {company_name}")
print(f"John Doe's Skills: {employee_skills}")

# Modifying nested data
data['employees'][1]['age'] = 26

print("Updated JSON data:")
print(json.dumps(data, indent=4))
