import datetime

def display_current_datetime():
    """
    Displays the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    # Get the current date and time
    current_date = datetime.datetime.now()
    # Format the current date and time
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date,
    and displays it in "YYYY-MM-DD" format.
    """
    try:
        # Prompt the user to enter a number of days
        num_of_days = int(input("Enter the number of days to add to the current date: "))
        
        # Get the current date (without time for simpler future date calculation)
        current_date_only = datetime.date.today()
        
        # Calculate the future date using timedelta
        future_date = current_date_only + datetime.timedelta(days=num_of_days)
        
        # Format the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

if __name__ == "__main__":
    # Call the function to display the current date and time
    display_current_datetime()
    print() # Add a blank line for better readability

    # Call the function to calculate and display a future date
    calculate_future_date()