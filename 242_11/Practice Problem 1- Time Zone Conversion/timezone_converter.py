from datetime import datetime
import pytz

def timezone_conversion():
    # Get current UTC time
    utc_now = datetime.now(pytz.utc)
    print(f"Current UTC time: {utc_now}")

    # Define target time zones
    eastern = pytz.timezone('US/Eastern')
    pacific = pytz.timezone('US/Pacific')

    # Convert UTC time to Eastern and Pacific time zones
    eastern_time = utc_now.astimezone(eastern)
    pacific_time = utc_now.astimezone(pacific)

    # Display results
    print(f"Current Eastern time: {eastern_time}")
    print(f"Current Pacific time: {pacific_time}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    timezone_conversion()
