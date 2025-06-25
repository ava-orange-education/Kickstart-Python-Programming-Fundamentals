import random 
# Initialize the game 
start, end = 1, 100 
secret_number = random.randint(start, end) 
guess = None 
# Begin the guessing game loop 
while guess != secret_number: 
    # Get user input 
    guess = int(input(f"Guess the number between {start} and {end}: ")) 
    # Evaluate the guess 
    if guess < secret_number: 
        print("Too low, try again!") 
    elif guess > secret_number: 
        print("Too high, try again!") 
    else: 
        # The guess is correct, congratulate the user 
        print("Congratulations! You guessed the correct number!") 
# Game over 
print("Thank you for playing the guessing game.") 
