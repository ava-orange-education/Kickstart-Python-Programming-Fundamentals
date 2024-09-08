def replace_char():
    # Prompt the user to enter a string
    user_input = input("Enter a string: ")
    # Prompt the user to enter the character to be replaced
    char_to_replace = input("Enter the character to replace: ")
    # Prompt the user to enter the replacement character
    replacement_char = input("Enter the replacement character: ")
    # Replace occurrences of the specified character with the replacement character
    modified_string = user_input.replace(char_to_replace, replacement_char)
    # Print the modified string
    print(f"Modified string: {modified_string}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    replace_char()
