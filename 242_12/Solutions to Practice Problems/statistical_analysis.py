import random
import statistics

def statistical_analysis():
    # Create a dataset of random numbers
    dataset = [random.randint(1, 100) for _ in range(100)]
    
    # Calculate the mean, median, mode, variance, and standard deviation of the dataset
    mean = statistics.mean(dataset)
    median = statistics.median(dataset)
    try:
        mode = statistics.mode(dataset)
    except statistics.StatisticsError:
        mode = "No unique mode found"
    variance = statistics.variance(dataset)
    std_deviation = statistics.stdev(dataset)
    
    # Print the results of each statistical measure
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_deviation}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    statistical_analysis()
