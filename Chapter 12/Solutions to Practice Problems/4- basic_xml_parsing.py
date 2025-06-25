import xml.etree.ElementTree as ET

def basic_xml_parsing():
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
    print("Original XML data:")
    print(ET.tostring(root, encoding='unicode'))
    
    # Modify XML data
    root.find('name').text = "Jane Doe"
    root.find('age').text = "25"
    graduation_year = ET.Element('graduationYear')
    graduation_year.text = "2022"
    root.append(graduation_year)
    root.remove(root.find('isStudent'))
    
    # Convert to XML string
    modified_xml_string = ET.tostring(root, encoding='unicode')
    print("Modified XML data:")
    print(modified_xml_string)

# Execute the function if the script is run directly
if __name__ == "__main__":
    basic_xml_parsing()
