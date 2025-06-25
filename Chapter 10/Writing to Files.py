# Using the 'with' statement for better resource management
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

#open it in append mode ("a")
with open("example.txt", "a") as file:
    file.write("Appending this line.\n")

#example of using writelines() 
lines = [
    "First line.\n",
    "Second line.\n",
    "Third line.\n"
]
with open("example.txt", "w") as file:
    file.writelines(lines)
