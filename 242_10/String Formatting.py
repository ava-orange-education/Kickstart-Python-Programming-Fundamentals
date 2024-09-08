#Using % Operator

name = "Alice"
age = 30
formatted_string = "Hello, %s! You are %d years old." % (name, age)
print(formatted_string)  # 'Hello, Alice! You are 30 years old.'

pi = 3.14159
formatted_pi = "The value of pi is %.2f" % pi
print(formatted_pi)  # 'The value of pi is 3.14'

#str.format() Method
name = "Bob"
age = 25
formatted_string = "Hello, {}! You are {} years old.".format(name, age)
print(formatted_string)  # 'Hello, Bob! You are 25 years old.'

# Positional arguments
formatted_string = "Hello, {0}! You are {1} years old.".format(name, age)
print(formatted_string)  # 'Hello, Bob! You are 25 years old.'

# Keyword arguments
formatted_string = "Hello, {name}! You are {age} years old.".format(name="Charlie", age=35)
print(formatted_string)  # 'Hello, Charlie! You are 35 years old.'

pi = 3.14159
formatted_pi = "The value of pi is {:.2f}".format(pi)
print(formatted_pi)  # 'The value of pi is 3.14'


#F-Strings (Formatted String Literals)
name = "Daisy"
age = 28
formatted_string = f"Hello, {name}! You are {age} years old."
print(formatted_string)  # 'Hello, Daisy! You are 28 years old.'

pi = 3.14159
formatted_pi = f"The value of pi is {pi:.2f}"
print(formatted_pi)  # 'The value of pi is 3.14'

# Using expressions
value = 42
formatted_expression = f"Twice the value is {value * 2}"
print(formatted_expression)  # 'Twice the value is 84'

    

