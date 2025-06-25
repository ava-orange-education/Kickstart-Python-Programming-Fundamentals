from datetime import datetime

def combine_and_format_datetime():
    # Step 1: Import the datetime Module
    # Already imported above

    # Step 2: Create a datetime Object
    original_datetime = datetime(2024, 7, 1, 14, 30, 0)
    print(f"Original datetime: {original_datetime}")

    # Step 3: Access and Modify Components
    year = original_datetime.year
    month = original_datetime.month
    day = original_datetime.day
    hour = original_datetime.hour
    minute = original_datetime.minute
    second = original_datetime.second

    # Create a new datetime object by modifying the year
    modified_datetime = original_datetime.replace(year=2025)
    print(f"Modified datetime: {modified_datetime}")

    # Step 4: Format the datetime Object
    formatted_original = original_datetime.strftime("%Y-%m-%d %H:%M:%S")
    formatted_modified = modified_datetime.strftime("%d/%m/%Y %I:%M %p")

    # Step 5: Display the Results
    print(f"Formatted original datetime: {formatted_original}")
    print(f"Formatted modified datetime: {formatted_modified}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    combine_and_format_datetime()
