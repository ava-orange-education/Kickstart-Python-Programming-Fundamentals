import json

def json_file_operations():
    # Read JSON data from file
    with open('input.json', 'r') as file:
        data = json.load(file)
    print("Original JSON data from file:", data)
    
    # Modify JSON data
    data['name'] = "Jane Doe"
    data['age'] = 25
    data['graduationYear'] = 2022
    
    # Write modified JSON data to a new file
    with open('output.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("Modified JSON data written to output.json")

# Execute the function if the script is run directly
if __name__ == "__main__":
    json_file_operations()
