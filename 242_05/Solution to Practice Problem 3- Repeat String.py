def repeat_string(s, n): 
    # Repeats the string 's' 'n' times. 
    # s: The string to repeat. 
    # n: The number of times to repeat the string. 
    return s * n # Multiplies the string 's' by 'n', effectively repeating it. 
# Repeating a simple greeting 3 times. 
print(repeat_string("Hi! ", 3)) # Outputs "Hi! Hi! Hi! " 
# Testing the function with an empty string and zero repetitions. 
print(repeat_string("", 5)) # Outputs an empty string. 
print(repeat_string("Python ", 0))  # Outputs: ""
print(repeat_string("!", 5))  # Outputs: "!!!!!"

