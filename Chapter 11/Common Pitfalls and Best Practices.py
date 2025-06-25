from datetime import datetime
import pytz

# Create timezone-aware datetime
utc = pytz.utc
now_utc = datetime.now(utc)

print(f"Current UTC time: {now_utc}")

eastern = pytz.timezone('US/Eastern')
dt = datetime(2024, 11, 3, 1, 30)
#dt_eastern = eastern.localize(dt, is_dst=None) # this will result in error
dt_eastern = eastern.localize(dt, is_dst=False) 
print(f"Localized Eastern Time: {dt_eastern}")

dt1 = datetime(2024, 7, 1, 12, 0, 0, tzinfo=pytz.UTC)
dt2 = datetime(2024, 7, 1, 8, 0, 0, tzinfo=pytz.timezone('US/Eastern'))
# Always compare timezone-aware datetime objects
print(f"UTC Time: {dt1}, Eastern Time: {dt2}")


dt = datetime.strptime("2024-07-01 14:30:00", "%Y-%m-%d %H:%M:%S")
formatted_date = dt.strftime("%B %d, %Y")
print(f"Formatted date: {formatted_date}")  # Output: July 01, 2024

from datetime import timedelta
future_date = datetime.now() + timedelta(days=10)
print(f"Future Date: {future_date}")

# Format a datetime in ISO 8601 format
iso_date = datetime.now().isoformat()
print(f"ISO 8601 Format: {iso_date}")


# Define a format string explicitly
dt = datetime.strptime("2024-07-01 14:30:00", "%Y-%m-%d %H:%M:%S")
print(f"Parsed datetime: {dt}")
