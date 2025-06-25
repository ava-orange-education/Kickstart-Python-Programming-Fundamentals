import xml.etree.ElementTree as ET

# XML string
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

# Parse XML string
root = ET.fromstring(xml_string)

# Accessing data
name = root.find('name').text
age = root.find('age').text
is_student = root.find('isStudent').text
courses = [course.text for course in root.find('courses').findall('course')]

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Is Student: {is_student}")
print(f"Courses: {courses}")
