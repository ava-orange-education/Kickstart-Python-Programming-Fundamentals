daily_steps = 0 
step_goal = 10000 
def track_daily_steps(steps): 
    # This function updates the global 'daily_steps' variable with the number of steps walked. 
    # steps: The number of steps to add to the daily total. 
    global daily_steps # Specifies that we're using the global variable 'daily_steps'. 
    # Add the new steps to the daily total. 
    daily_steps += steps 
    # Check if the daily step goal has been met or exceeded. 
    if daily_steps >= step_goal: 
        print("Congratulations! You've reached your daily step goal!") 
    else: 
        remaining = step_goal - daily_steps 
        print(f"Great job! You need {remaining} more steps to reach your daily goal.") 
# Simulating adding steps throughout the day. 
track_daily_steps(3000) # Outputs: "Great job! You need 7000 more steps to reach your daily goal." 
track_daily_steps(4500) # Outputs: "Great job! You need 2500 more steps to reach your daily goal." 
track_daily_steps(3000) # Outputs: "Congratulations! You've reached your daily step goal!" 
