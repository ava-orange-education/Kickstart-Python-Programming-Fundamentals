from datetime import datetime
import pytz

# Define time zones
utc = pytz.utc
eastern = pytz.timezone('US/Eastern')
pacific = pytz.timezone('US/Pacific')

# Current time in UTC
utc_now = datetime.now(utc)
print(f"Current UTC time: {utc_now}")

# Convert UTC time to Eastern time
eastern_now = utc_now.astimezone(eastern)
print(f"Current Eastern time: {eastern_now}")

# Convert Eastern time to Pacific time
pacific_now = eastern_now.astimezone(pacific)
print(f"Current Pacific time: {pacific_now}")
########################################################

# Define a time in Eastern time zone
eastern = pytz.timezone('US/Eastern')
dt = datetime(2024, 11, 3, 1, 30)  # November 3, 2024, 1:30 AM

# Localize the time to Eastern time zone
dt_eastern = eastern.localize(dt, is_dst=True)
print(f"Localized time: {dt_eastern}")

# Convert to UTC
dt_utc = dt_eastern.astimezone(pytz.utc)
print(f"Converted to UTC: {dt_utc}")


