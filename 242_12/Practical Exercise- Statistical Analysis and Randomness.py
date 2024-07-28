import random
import statistics

def generate_dataset(size):
    """Generate a dataset of random numbers."""
    return [random.randint(1, 100) for _ in range(size)]

def analyze_dataset(data):
    """Calculate statistical measures for the dataset."""
    mean = statistics.mean(data)
    median = statistics.median(data)
    try:
        mode = statistics.mode(data)
    except statistics.StatisticsError:
        mode = "No unique mode found"
    variance = statistics.variance(data)
    std_deviation = statistics.stdev(data)

    return mean, median, mode, variance, std_deviation

def simulate_randomness():
    """Simulate random events."""
    random_float = random.random()
    random_int = random.randint(1, 10)
    random_choice = random.choice(['apple', 'banana', 'cherry'])
    random_sample = random.sample(range(1, 100), 5)
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    random_gaussian = random.gauss(0, 1)

    return random_float, random_int, random_choice, random_sample, numbers, random_gaussian

def display_results(mean, median, mode, variance, std_deviation, randomness):
    """Display the results of the statistical analysis and randomness simulation."""
    print("Statistical Analysis of Dataset:")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_deviation}")
    print("\nRandomness Simulation:")
    print(f"Random Float: {randomness[0]}")
    print(f"Random Integer: {randomness[1]}")
    print(f"Random Choice: {randomness[2]}")
    print(f"Random Sample: {randomness[3]}")
    print(f"Shuffled List: {randomness[4]}")
    print(f"Random Gaussian: {randomness[5]}")

def main():
    dataset = generate_dataset(100)
    mean, median, mode, variance, std_deviation = analyze_dataset(dataset)
    randomness = simulate_randomness()
    display_results(mean, median, mode, variance, std_deviation, randomness)

if __name__ == "__main__":
    main()
