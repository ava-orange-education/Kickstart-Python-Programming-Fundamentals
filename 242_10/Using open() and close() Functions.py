# Opening a file
file = open("./data/example.txt", "r")  # 'r' mode opens the file for reading

# Performing operations (e.g., reading the file content)
content = file.read()
print(content)

# Closing the file
file.close()
