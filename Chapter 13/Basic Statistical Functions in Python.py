import statistics

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)  # This will raise a StatisticsError if no mode is found
variance = statistics.variance(data)
std_deviation = statistics.stdev(data)

print(f"Mean: {mean}")  # Output: 5.5
print(f"Median: {median}")  # Output: 5.5
print(f"Mode: {mode}")  # Output: (will raise error if no mode)
print(f"Variance: {variance}")  # Output: 9.166666666666666
print(f"Standard Deviation: {std_deviation}")  # Output: 3.0276503540974917
