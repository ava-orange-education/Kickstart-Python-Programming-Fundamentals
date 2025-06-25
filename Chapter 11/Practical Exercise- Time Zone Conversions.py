# Step 1: Install the pytz Library
# Make sure to install the pytz library if you haven't already
# You can install it using the command: pip install pytz

# Step 2: Import Required Modules
from datetime import datetime
import pytz

def main():
    # Step 3: Get Current UTC Time
    utc_now = datetime.now(pytz.utc)
    print(f"Current UTC time: {utc_now}")

    # Step 4: Define Target Time Zones
    eastern = pytz.timezone('US/Eastern')
    pacific = pytz.timezone('US/Pacific')

    # Step 5: Perform Time Zone Conversions
    eastern_time = utc_now.astimezone(eastern)
    pacific_time = utc_now.astimezone(pacific)

    # Step 6: Display the Results
    print(f"Current Eastern time: {eastern_time}")
    print(f"Current Pacific time: {pacific_time}")

if __name__ == "__main__":
    main()
