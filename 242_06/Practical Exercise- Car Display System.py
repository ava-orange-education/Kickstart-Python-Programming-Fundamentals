# Define the Car class 
class Car: 
    # Class attributes 
    color = 'White' 
    make = 'Generic Make' 
    @classmethod 
    def display_info(cls): 
        print(f"The car is a {cls.color} {cls.make}.") 

    @classmethod 
    def change_color(cls, new_color): 
        cls.color = new_color 

    @classmethod 
    def change_make(cls, new_make): 
        cls.make = new_make 
# Main interaction loop
while True: 
    # Display the menu options 
    print("\n1. Show car info") 
    print("2. Change car color") 
    print("3. Change car make") 
    print("4. Exit") 
    choice = input("Enter your choice: ") 
    if choice == '1': 
        # Display current car information 
        Car.display_info() 
    elif choice == '2':
        # Prompt for a new color and update the class attribute 
        new_color = input("Enter the new color for the car: ") 
        Car.change_color(new_color) 
        print("Car color updated.") 
    elif choice == '3': 
        # Prompt for a new make and update the class attribute 
        new_make = input("Enter the new make for the car: ") 
        Car.change_make(new_make) 
        print("Car make updated.") 
    elif choice == '4': 
        # Exit the program 
        print("Exiting program.") 
        break 
    else: 
        # Handle invalid menu options 
        print("Invalid choice. Please choose a valid option.")
