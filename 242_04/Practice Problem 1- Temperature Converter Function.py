def convert_temperature(temp, unit): 
    # This function converts temperatures between Celsius and Fahrenheit. 
    # temp: The temperature value you want to convert. 
    # unit: The unit of the input temperature ('C' for Celsius, 'F' for Fahrenheit). 
    if unit == "C": 
        return (temp * 9/5) + 32 # Formula to convert Celsius to Fahrenheit. 
    elif unit == "F": 
        return (temp - 32) * 5/9 # Formula to convert Fahrenheit to Celsius. 
    else: 
        return "Invalid unit" # If the unit isn't 'C' or 'F', return an error message. 
# Testing the function with a temperature in Celsius. 
print(convert_temperature(0, "C")) # Outputs 32, converting 0°C to Fahrenheit. 
# Testing the function with a temperature in Fahrenheit. 
print(convert_temperature(32, "F")) # Outputs 0, converting 32°F to Celsius. 
