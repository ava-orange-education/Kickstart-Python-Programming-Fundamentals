from datetime import datetime, timedelta

def date_arithmetic():
    # Get the current date
    today = datetime.now().date()
    print(f"Today's date: {today}")

    # Calculate the date 10 days from today
    future_date = today + timedelta(days=10)
    print(f"Date 10 days from today: {future_date}")

    # Calculate the date 10 days before today
    past_date = today - timedelta(days=10)
    print(f"Date 10 days before today: {past_date}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    date_arithmetic()
