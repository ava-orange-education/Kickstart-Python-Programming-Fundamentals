def greet():
    message = "Hello, Python!"  # Local variable
    print(message)

greet()  # Outputs: Hello, Python!

print(message)  # This will cause an error because 'message' is not accessible outside the function.
