def read_file_line_by_line():
    # Prompt the user to enter the filename
    filename = input("Enter the filename: ")
    try:
        # Attempt to open the file in read mode
        with open(filename, "r") as file:
            # Read the first line from the file
            line = file.readline()
            # Loop through the file until the end is reached
            while line:
                # Print the line after stripping leading/trailing whitespace
                print(line.strip())
                # Read the next line from the file
                line = file.readline()
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("Error: File not found.")
    except IOError as e:
        # Handle other I/O errors
        print(f"Error reading file: {e}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    read_file_line_by_line()

