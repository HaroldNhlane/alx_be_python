# explore_datetime.py

import datetime

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days and calculates a future date.

    Args:
        current_date (datetime): The starting date for calculation.

    Returns:
        datetime: The calculated future date.
    """
    while True:
        try:
            num_days_str = input("Enter the number of days to add to the current date: ")
            num_days = int(num_days_str)
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    future_date = current_date + datetime.timedelta(days=num_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

if __name__ == "__main__":
    current_dt = display_current_datetime()
    calculate_future_date(current_dt)