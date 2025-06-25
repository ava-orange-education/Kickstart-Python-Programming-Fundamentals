# Global variable to track the highest score 
high_score = 0 
# Function to update the high score 
def update_high_score(new_score): 
    global high_score 
    if new_score > high_score: 
        high_score = new_score 
        print(f"New high score: {high_score}") 
    else: 
        print(f"Current high score remains: {high_score}") 
# Main loop to enter new scores 
while True: 
    score_input = input("Enter a new score (or type 'exit' to quit): ") 
    if score_input.lower() == 'exit': 
        print("Exiting. Final high score:", high_score) 
        break 
    else: 
        new_score = int(score_input) 
        update_high_score(new_score) 
