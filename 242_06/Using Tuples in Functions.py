def get_dimensions(): 
# Return multiple values in a tuple 
    print('Enter width:')
    width = input()
    print('Enter height:')
    height = input()
    return (width, height) 
dimensions = get_dimensions() 

def concat_strings(*args): 
    return ' '.join(args) 
result = concat_strings("Hello", "world", "!") # Outputs: "Hello world !" 
