from datetime import datetime

def timestamp_converter():
    # Get the current time
    now = datetime.now()
    print(f"Current datetime: {now}")

    # Convert the current time to a timestamp
    timestamp = now.timestamp()
    print(f"Current timestamp: {timestamp}")

    # Convert the timestamp back to a datetime object
    dt_from_timestamp = datetime.fromtimestamp(timestamp)
    print(f"Datetime from timestamp: {dt_from_timestamp}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    timestamp_converter()
