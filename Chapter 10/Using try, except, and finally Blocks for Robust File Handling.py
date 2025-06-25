try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print(f"Error: File not found. {e}")
except PermissionError as e:
    print(f"Error: Permission denied. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    try:
        file.close()
    except NameError:
        pass  # File was not opened, so no need to close it
