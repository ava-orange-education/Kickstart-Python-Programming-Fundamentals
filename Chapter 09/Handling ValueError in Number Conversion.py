try:
    value = int('abc')
except ValueError:
    print("Handled value error when converting string to integer.")
