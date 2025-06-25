import xml.etree.ElementTree as ET

# Parse XML string
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

# Parse XML string
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

# Adding a new skill to an employee
new_skill = ET.Element('skill')
new_skill.text = "Project Management"
employee_to_modify.find('skills').append(new_skill)

# Displaying modified XML
print(ET.tostring(root, encoding='unicode'))
