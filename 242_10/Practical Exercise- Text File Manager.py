def create_file(filename):
    try:
        with open(filename, "w") as file:
            file.write("This is a new file.\n")
        print("File created successfully.")
    except IOError as e:
        print(f"Error creating file: {e}")

def write_to_file(filename, data):
    try:
        with open(filename, "a") as file:
            file.write(data + "\n")
        print("Data written successfully.")
    except IOError as e:
        print(f"Error writing to file: {e}")

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError as e:
        print(f"Error: File not found. {e}")
    except IOError as e:
        print(f"Error reading file: {e}")

def main():
    while True:
        print("\nText File Manager")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter the filename: ")
            create_file(filename)
        elif choice == '2':
            filename = input("Enter the filename: ")
            data = input("Enter the data to write: ")
            write_to_file(filename, data)
        elif choice == '3':
            filename = input("Enter the filename: ")
            read_file(filename)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
