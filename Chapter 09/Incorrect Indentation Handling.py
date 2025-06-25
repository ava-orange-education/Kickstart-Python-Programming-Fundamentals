# IndentationError cannot be caught by try-except because it's a syntax error that occurs before execution.
# Corrected version:
try:
    if True:  # Added colon
        print("This will run.")
except IndentationError:
    print("This line will never be reached.")
