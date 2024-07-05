# word_frequency.py

from collections import Counter

def count_word_frequency():
    # Prompt the user to enter the filename
    filename = input("Enter the filename: ")
    try:
        # Attempt to open the file in read mode
        with open(filename, "r") as file:
            # Read the entire content of the file
            content = file.read()
            # Split the content into words
            words = content.split()
            # Count the frequency of each word using Counter from collections module
            word_count = Counter(words)
            # Print the word frequencies
            for word, count in word_count.items():
                print(f"{word}: {count}")
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("Error: File not found.")
    except IOError as e:
        # Handle other I/O errors
        print(f"Error reading file: {e}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    count_word_frequency()
