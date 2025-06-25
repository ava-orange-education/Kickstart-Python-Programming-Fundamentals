# Define the Participant class with a constructor 
class Participant: 
    def __init__(self, name, email): 
        self.name = name 
        self.email = email 
    def __str__(self): 
        return f"{self.name} ({self.email})" 
# Initialize the list of participants 
participants = [] 
# Main interaction loop 
while True: 
    print("\n1. Add a participant") 
    print("2. Remove a participant") 
    print("3. Show all participants") 
    print("4. Exit") 
    choice = input("Enter your choice: ") 
    if choice == '1': 
        name = input("Enter the participant's name: ") 
        email = input("Enter the participant's email: ") 
        participants.append(Participant(name, email)) 
        print("Participant added.") 
    elif choice == '2':
        email = input("Enter the email of the participant to remove: ") 
        found = False 
        for participant in participants: 
            if participant.email == email: 
                participants.remove(participant) 
                print("Participant removed.") 
                found = True 
                break 
        if not found: 
            print("Participant not found.") 
        elif choice == '3': 
            if participants: 
                print("Registered Participants:") 
                for participant in participants: 
                    print(participant) 
            else: print("No participants registered.") 
        elif choice == '4': 
            print("Exiting program.") 
            break 
        else: 
            print("Invalid choice. Please choose a valid option.") 
