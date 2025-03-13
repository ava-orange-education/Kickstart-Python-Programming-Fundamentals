import xml.etree.ElementTree as ET

def load_xml_from_string():
    xml_string = '''
    <person>
      <name>John Doe</name>
      <age>30</age>
      <isStudent>false</isStudent>
      <courses>
        <course>Python</course>
        <course>Data Science</course>
      </courses>
    </person>
    '''
    return ET.fromstring(xml_string)

def load_xml_from_file(file_path):
    tree = ET.parse(file_path)
    return tree.getroot()

def access_and_modify_xml(data):
    # Accessing data
    name = data.find('name').text
    courses = [course.text for course in data.find('courses').findall('course')]
    city = data.find('address/city').text if data.find('address/city') is not None else "N/A"
    
    print(f"Name: {name}")
    print(f"Courses: {courses}")
    print(f"City: {city}")
    
    # Modifying data
    data.find('name').text = "Jane Doe"
    age = data.find('age')
    if age is not None:
        age.text = "25"
    else:
        age = ET.SubElement(data, 'age')
        age.text = "25"
    
    graduation_year = ET.Element('graduationYear')
    graduation_year.text = "2022"
    data.append(graduation_year)
    
    is_student = data.find('isStudent')
    if is_student is not None:
        data.remove(is_student)

    return data

def generate_xml_tree():
    # Create root element
    root = ET.Element('company')
    
    # Create nested elements
    employees = ET.SubElement(root, 'employees')
    employee1 = ET.SubElement(employees, 'employee', id='1')
    ET.SubElement(employee1, 'name').text = "John Doe"
    ET.SubElement(employee1, 'age').text = "30"
    skills1 = ET.SubElement(employee1, 'skills')
    ET.SubElement(skills1, 'skill').text = "Python"
    ET.SubElement(skills1, 'skill').text = "Data Analysis"
    
    employee2 = ET.SubElement(employees, 'employee', id='2')
    ET.SubElement(employee2, 'name').text = "Jane Smith"
    ET.SubElement(employee2, 'age').text = "25"
    skills2 = ET.SubElement(employee2, 'skills')
    ET.SubElement(skills2, 'skill').text = "JavaScript"
    ET.SubElement(skills2, 'skill').text = "Web Development"
    
    ET.SubElement(root, 'location').text = "Silicon Valley"
    
    return root

def convert_to_xml_string(root):
    return ET.tostring(root, encoding='unicode')

def write_xml_to_file(root, file_path):
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='unicode', xml_declaration=True)

def handle_complex_xml():
    xml_string = '''
    <company>
      <employees>
        <employee id="1">
          <name>John Doe</name>
          <age>30</age>
          <skills>
            <skill>Python</skill>
            <skill>Data Analysis</skill>
          </skills>
        </employee>
        <employee id="2">
          <name>Jane Smith</name>
          <age>25</age>
          <skills>
            <skill>JavaScript</skill>
            <skill>Web Development</skill>
          </skills>
        </employee>
      </employees>
      <location>Silicon Valley</location>
    </company>
    '''
    
    root = ET.fromstring(xml_string)
    
    # Accessing nested data
    employees = root.find('employees')
    for employee in employees.findall('employee'):
        name = employee.find('name').text
        age = employee.find('age').text
        skills = [skill.text for skill in employee.find('skills').findall('skill')]
        print(f"Name: {name}, Age: {age}, Skills: {skills}")
    
    # Modifying nested data
    employee_to_modify = employees.find("employee[@id='2']")
    employee_to_modify.find('age').text = "26"
    
    new_skill = ET.Element('skill')
    new_skill.text = "Project Management"
    employee_to_modify.find('skills').append(new_skill)
    
    return root

def main():
    # Load XML from string
    data_from_string = load_xml_from_string()
    print("Loaded XML from string:")
    print(convert_to_xml_string(data_from_string))

    # Load XML from file
    file_path = './example xml/Simple Xml Data.xml'  # Ensure this file exists with valid XML data
    data_from_file = load_xml_from_file(file_path)
    print("\nLoaded XML from file:")
    print(convert_to_xml_string(data_from_file))

    # Access and modify XML data
    modified_data = access_and_modify_xml(data_from_file)
    print("\nModified XML data:")
    print(convert_to_xml_string(modified_data))

    # Write modified XML to a new file
    output_file_path = 'modified_data.xml'
    write_xml_to_file(modified_data, output_file_path)
    print(f"\nModified XML data written to {output_file_path}")

    # Generate and handle complex XML structure
    complex_xml_root = generate_xml_tree()
    complex_data = handle_complex_xml()
    print("\nHandled complex XML data:")
    print(convert_to_xml_string(complex_data))

if __name__ == "__main__":
    main()
