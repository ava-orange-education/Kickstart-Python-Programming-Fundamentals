import xml.etree.ElementTree as ET

def xml_file_operations():
    # Read XML data from file
    tree = ET.parse('input.xml')
    root = tree.getroot()
    print("Original XML data from file:")
    print(ET.tostring(root, encoding='unicode'))
    
    # Modify XML data
    root.find('name').text = "Jane Doe"
    root.find('age').text = "25"
    graduation_year = ET.Element('graduationYear')
    graduation_year.text = "2022"
    root.append(graduation_year)
    is_student = root.find('isStudent')
    if is_student is not None:
        root.remove(is_student)
    
    # Write modified XML data to a new file
    tree.write('output.xml', encoding='unicode', xml_declaration=True)
    print("Modified XML data written to output.xml")

# Execute the function if the script is run directly
if __name__ == "__main__":
    xml_file_operations()
