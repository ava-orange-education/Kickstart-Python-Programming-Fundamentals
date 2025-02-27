# Import the custom utilities module 
from utilities import celsius_to_fahrenheit, fahrenheit_to_celsius
# Test the temperature conversion functions 
# Convert 100 degrees Fahrenheit to Celsius 
temp_in_celsius = fahrenheit_to_celsius(100) 
print(f"100 degrees Fahrenheit is {temp_in_celsius:.2f} degrees Celsius.") 
# Convert 37 degrees Celsius to Fahrenheit 
temp_in_fahrenheit = celsius_to_fahrenheit(37) 
print(f"37 degrees Celsius is {temp_in_fahrenheit:.2f} degrees Fahrenheit.")
