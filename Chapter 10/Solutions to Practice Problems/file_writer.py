def write_to_file():
    # Prompt the user to enter the filename
    filename = input("Enter the filename: ")
    # Prompt the user to enter the text to write to the file
    data = input("Enter the text to write to the file: ")
    try:
        # Attempt to open the file in append mode
        with open(filename, "a") as file:
            # Write the user input to the file followed by a newline character
            file.write(data + "\n")
        # Inform the user that the data was written successfully
        print("Data written successfully.")
    except IOError as e:
        # Handle I/O errors
        print(f"Error writing to file: {e}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    write_to_file()
