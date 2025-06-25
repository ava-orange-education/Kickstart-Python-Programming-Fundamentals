def write_data_to_file(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)
        print("Data written successfully.")
    except PermissionError as e:
        print(f"Error: Permission denied. {e}")
    except IOError as e:
        print(f"Error: I/O error occurred. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
data = "Hello, World!"
write_data_to_file("output.txt", data)
