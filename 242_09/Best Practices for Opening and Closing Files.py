with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# No need to explicitly call file.close(); it is automatically closed
