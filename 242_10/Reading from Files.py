# Using the 'with' statement for better resource management
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())  # strip() removes the newline character
        line = file.readline()
        
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes the newline character
