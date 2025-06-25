try:
    dict = {'key': 'value'}
    print(dict['nonexistentkey'])
except KeyError:
    print("Handled missing key in dictionary.")
