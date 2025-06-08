from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(current_date):
    while True:
        try:
            num_days_str = input("Enter the number of days to add to the current date: ")
            num_days = int(num_days_str)
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    future_date = current_date + timedelta(days=num_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date