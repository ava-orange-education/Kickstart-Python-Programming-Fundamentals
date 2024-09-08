# Initialize the list of tasks 
tasks = [] 
while True: 
    # Display the menu options 
    print("\n1. Add a task") 
    print("2. Remove a task") 
    print("3. Show all tasks") 
    print("4. Exit") 
    choice = input("Enter your choice: ") 
    if choice == '1': 
        # Prompt for a new task and add it to the list 
        task = input("What task would you like to add? ") 
        tasks.append(task) 
        print("Task added.") 
    elif choice == '2': 
        # Prompt for the task to remove and attempt to remove it 
        task = input("What task would you like to remove? ") 
        if task in tasks: 
            tasks.remove(task) 
            print("Task removed.") 
        else: print("Task not found.") 
    elif choice == '3': 
        # Display all current tasks 
        print("Current Tasks:") 
        for task in tasks: 
            print(task) 
    elif choice == '4': 
        # Exit the program 
        print("Exiting program.") 
        break 
    else: # Handle invalid menu options 
        print("Invalid choice. Please choose a valid option.") 
