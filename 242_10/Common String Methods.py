#upper(): Converts all characters in the string to uppercase.
my_string = "Hello, World!"
upper_string = my_string.upper()
print(upper_string)  # 'HELLO, WORLD!'

#lower(): Converts all characters in the string to lowercase.
my_string = "Hello, World!"
lower_string = my_string.lower()
print(lower_string)  # 'hello, world!'

#strip(): Removes leading and trailing whitespace from the string. You can also specify characters to remove.
my_string = "   Hello, World!   "
stripped_string = my_string.strip()
print(stripped_string)  # 'Hello, World!'

# Removing specific characters
char_string = "###Hello###"
stripped_char_string = char_string.strip("#")
print(stripped_char_string)  # 'Hello'

#replace(): Replaces all occurrences of a specified substring with another substring.
my_string = "Hello, World!"
replaced_string = my_string.replace("World", "Python")
print(replaced_string)  # 'Hello, Python!'

#find(): Returns the index of the first occurrence of a specified substring. Returns -1 if the substring is not found.
my_string = "Hello, World!"
index = my_string.find("World")
print(index)  # 7

#split(): Splits the string into a list of substrings based on a specified delimiter. The default delimiter is any whitespace.
my_string = "Hello, World!"
split_string = my_string.split(", ")
print(split_string)  # ['Hello', 'World!']

# Splitting by whitespace
whitespace_string = "Hello World"
split_whitespace_string = whitespace_string.split()
print(split_whitespace_string)  # ['Hello', 'World']

#join(): Joins a list of strings into a single string, with a specified separator.
list_of_strings = ["Hello", "World"]
joined_string = ", ".join(list_of_strings)
print(joined_string)  # 'Hello, World'

#startswith() and endswith(): Checks if the string starts or ends with a specified substring.
my_string = "Hello, World!"
starts_with_hello = my_string.startswith("Hello")
print(starts_with_hello)  # True

ends_with_world = my_string.endswith("World!")
print(ends_with_world)  # True
