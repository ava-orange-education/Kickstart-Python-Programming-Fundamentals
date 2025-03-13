import xml.etree.ElementTree as ET

# Parse XML file
tree = ET.parse('./example xml/Simple Xml Data.xml')
root = tree.getroot()

# Accessing data
print(root.find('name').text)  # Output: John Doe
print(root.find('age').text)   # Output: 30
