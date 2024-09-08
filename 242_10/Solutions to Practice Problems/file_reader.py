def read_file():
    # Prompt the user to enter the filename
    filename = input("Enter the filename: ")
    try:
        # Attempt to open the file in read mode
        with open(filename, "r") as file:
            # Read the entire content of the file
            content = file.read()
            # Print the content of the file
            print(content)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("Error: File not found.")
    except IOError as e:
        # Handle other I/O errors
        print(f"Error reading file: {e}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    read_file()
