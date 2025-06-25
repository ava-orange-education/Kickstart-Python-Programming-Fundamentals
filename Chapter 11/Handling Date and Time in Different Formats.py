from datetime import datetime

# Current time as a timestamp
timestamp_now = datetime.now().timestamp()
print(f"Current timestamp: {timestamp_now}")

# Convert timestamp to datetime
dt_from_timestamp = datetime.fromtimestamp(timestamp_now)
print(f"Datetime from timestamp: {dt_from_timestamp}")


from datetime import datetime

date_string = "2024-07-01 14:30:00"
format_string = "%Y-%m-%d %H:%M:%S"
parsed_date = datetime.strptime(date_string, format_string)
print(f"Parsed datetime: {parsed_date}")


from datetime import datetime

# Current datetime
now = datetime.now()

# Format datetime into a string
formatted_date = now.strftime("%B %d, %Y %I:%M %p")
print(f"Formatted date: {formatted_date}")


from datetime import datetime

date_string = "July 01, 2024 02:30 PM"
format_string = "%B %d, %Y %I:%M %p"
parsed_date = datetime.strptime(date_string, format_string)
print(f"Parsed datetime: {parsed_date}")


from datetime import datetime

# Current datetime
now = datetime.now()

# Format datetime into a string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date: {formatted_date}")
