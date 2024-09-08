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
print(root.find('name').text)  # Output: John Doe
print(root.find('age').text)   # Output: 30
