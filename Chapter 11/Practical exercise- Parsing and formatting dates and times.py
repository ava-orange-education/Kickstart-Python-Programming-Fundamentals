from datetime import datetime

def main():
    # Step 1: Import the datetime Module
    # The datetime module is used to create and manipulate date objects

    # Step 2: Define a Date String
    date_string = "July 01, 2024 02:30 PM"
    format_string = "%B %d, %Y %I:%M %p"
    
    # Step 3: Parse the Date String
    parsed_date = datetime.strptime(date_string, format_string)
    print(f"Original date string: {date_string}")
    print(f"Parsed datetime: {parsed_date}")

    # Step 4: Format the datetime Object
    # Format to "YYYY-MM-DD HH:MM:SS"
    formatted_date1 = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Formatted date 1: {formatted_date1}")

    # Format to "DD/MM/YYYY"
    formatted_date2 = parsed_date.strftime("%d/%m/%Y")
    print(f"Formatted date 2: {formatted_date2}")

    # Format to "Month Day, Year"
    formatted_date3 = parsed_date.strftime("%B %d, %Y")
    print(f"Formatted date 3: {formatted_date3}")

    # Format to "Day-Month-Year Hour:Minute AM/PM"
    formatted_date4 = parsed_date.strftime("%d-%B-%Y %I:%M %p")
    print(f"Formatted date 4: {formatted_date4}")

if __name__ == "__main__":
    main()
