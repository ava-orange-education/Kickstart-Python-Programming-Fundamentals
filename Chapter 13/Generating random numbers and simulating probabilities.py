import random

# Generating random numbers
random_float = random.random()
random_int = random.randint(1, 10)
random_choice = random.choice(['apple', 'banana', 'cherry'])
random_sample = random.sample(range(1, 100), 5)
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
random_gaussian = random.gauss(0, 1)

print(f"Random Float: {random_float}")  # Output: Random float between 0.0 and 1.0
print(f"Random Integer: {random_int}")  # Output: Random integer between 1 and 10
print(f"Random Choice: {random_choice}")  # Output: Randomly chosen element from list
print(f"Random Sample: {random_sample}")  # Output: Random list of 5 unique numbers
print(f"Shuffled List: {numbers}")  # Output: Shuffled list of numbers
print(f"Random Gaussian: {random_gaussian}")  # Output: Random float from Gaussian distribution
