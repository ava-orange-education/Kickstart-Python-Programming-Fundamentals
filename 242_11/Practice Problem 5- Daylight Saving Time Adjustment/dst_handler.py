from datetime import datetime
import pytz

def dst_handler():
    # Define a specific date and time in the US/Eastern time zone
    eastern = pytz.timezone('US/Eastern')
    dt = datetime(2024, 11, 3, 1, 30)
    
    # Localize the time to Eastern time zone considering DST
    dt_eastern = eastern.localize(dt, is_dst=None)
    print(f"Localized time: {dt_eastern}")

    # Convert the localized time to UTC
    dt_utc = dt_eastern.astimezone(pytz.utc)
    print(f"Converted to UTC: {dt_utc}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    dst_handler()
