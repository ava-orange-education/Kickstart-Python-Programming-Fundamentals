import arithmetic 
def main(): 
    num1 = float(input("Enter the first number: ")) 
    num2 = float(input("Enter the second number: ")) 
    operation = input("Choose the operation (add, subtract, multiply, divide): ").lower() 
    operations = { 'add': arithmetic.add, 'subtract': arithmetic.subtract, 
                  'multiply': arithmetic.multiply, 'divide': arithmetic.divide } 
    if operation in operations: 
        result = operations[operation](num1, num2) 
        print(f"The result is: {result}") 
    else: 
        print("Invalid operation selected!") 
if __name__ == "__main__": main()  
