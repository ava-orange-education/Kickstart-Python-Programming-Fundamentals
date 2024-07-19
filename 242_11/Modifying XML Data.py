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

# Modifying existing data
root.find('name').text = "Jane Doe"
root.find('age').text = "25"

# Adding new data
graduation_year = ET.Element('graduationYear')
graduation_year.text = "2022"
root.append(graduation_year)

# Removing data
root.remove(root.find('isStudent'))

# Displaying modified XML
print(ET.tostring(root, encoding='unicode'))
