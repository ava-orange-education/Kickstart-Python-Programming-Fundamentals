import xml.etree.ElementTree as ET

# Create root element
root = ET.Element('person')

# Create child elements
name = ET.SubElement(root, 'name')
name.text = "John Doe"

age = ET.SubElement(root, 'age')
age.text = "30"

courses = ET.SubElement(root, 'courses')
course1 = ET.SubElement(courses, 'course')
course1.text = "Python"
course2 = ET.SubElement(courses, 'course')
course2.text = "Data Science"



# Converting to XML string
xml_string = ET.tostring(root, encoding='unicode')
print(xml_string)
