from datetime import datetime

def parse_format_dates():
    # Define a date string
    date_string = "July 01, 2024 02:30 PM"
    format_string = "%B %d, %Y %I:%M %p"
    
    # Parse the date string into a datetime object
    parsed_date = datetime.strptime(date_string, format_string)
    print(f"Original date string: {date_string}")
    print(f"Parsed datetime: {parsed_date}")

    # Format the datetime object into different string representations
    formatted_date1 = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Formatted date 1: {formatted_date1}")

    formatted_date2 = parsed_date.strftime("%d/%m/%Y")
    print(f"Formatted date 2: {formatted_date2}")

    formatted_date3 = parsed_date.strftime("%B %d, %Y")
    print(f"Formatted date 3: {formatted_date3}")

    formatted_date4 = parsed_date.strftime("%d-%B-%Y %I:%M %p")
    print(f"Formatted date 4: {formatted_date4}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    parse_format_dates()
