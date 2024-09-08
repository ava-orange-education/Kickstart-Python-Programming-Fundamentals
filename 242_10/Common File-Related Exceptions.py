#FileNotFoundError: Raised when trying to open a file that does not exist.
try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError as e:
    print(f"Error: {e}")

#PermissionError: Raised when the file operation fails due to insufficient permissions.
try:
    file = open("/restricted_access_file.txt", "r")
except PermissionError as e:
    print(f"Error: {e}")

#IsADirectoryError: Raised when a directory is being used as a file.
try:
    file = open("/path_to_directory", "r")
except IsADirectoryError as e:
    print(f"Error: {e}")

#IOError: Raised when an input/output operation fails. This is a more general error that can encompass issues like a full disk or hardware failure.
try:
    file = open("file.txt", "r")
    content = file.read()
except IOError as e:
    print(f"Error: {e}")
