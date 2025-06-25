while True: 
    # Presenting the menu to the user 
    print("\nMenu:") 
    print("1. Display a greeting message") 
    print("2. Exit") 
    # Getting user input 
    choice = input("Please enter your choice (1 or 2): ") 
    # Implementing Conditional Logic 
    if choice == '1': 
        #Option 1: Perform an action 
        print("Hello, world!") 
    elif choice == '2': 
        # Option 2: Exit the program 
        print("Goodbye!") 
        break 
    else: 
        # Handling invalid input 
        print("Invalid choice, please choose 1 or 2.")  
