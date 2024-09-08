try:
    file = open('nonexistentfile.txt', 'r')
except FileNotFoundError:
    print("Handled file not found error.")
