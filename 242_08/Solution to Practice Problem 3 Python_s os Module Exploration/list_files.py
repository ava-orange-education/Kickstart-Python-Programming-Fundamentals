# Script to list files and directories using os module
import os

# List all files and directories in the current directory
for item in os.listdir('.'):
    print(item)  # Print each item found in the directory

# Bonus: Find and print Python files
for item in os.listdir('.'):
    if item.endswith('.py'):
        print(f"Python file: {item}")  # Prints only Python files