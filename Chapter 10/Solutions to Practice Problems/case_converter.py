def case_conversion():
    # Prompt the user to enter a string
    user_input = input("Enter a string: ")
    # Convert the string to uppercase
    upper_case = user_input.upper()
    # Convert the string to lowercase
    lower_case = user_input.lower()
    # Print the converted strings
    print(f"Uppercase: {upper_case}")
    print(f"Lowercase: {lower_case}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    case_conversion()

