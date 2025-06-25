import re

def search_regex():
    # Prompt the user to enter the filename
    filename = input("Enter the filename: ")
    # Prompt the user to enter the regex pattern
    pattern = input("Enter the regex pattern: ")
    try:
        # Attempt to open the file in read mode
        with open(filename, "r") as file:
            # Read the entire content of the file
            content = file.read()
            # Search for all matches of the regex pattern in the content
            matches = re.findall(pattern, content)
            if matches:
                # Print the matches found
                print("Matches found:")
                for match in matches:
                    print(match)
            else:
                # Inform the user that no matches were found
                print("No matches found.")
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("Error: File not found.")
    except re.error as e:
        # Handle invalid regex patterns
        print(f"Error: Invalid regex pattern. {e}")
    except IOError as e:
        # Handle other I/O errors
        print(f"Error reading file: {e}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    search_regex()
