# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message part for time sensitivity
time_sensitive_message = ""

# Check if the task is time-bound
if time_bound == 'yes':
    time_sensitive_message = " that requires immediate attention today!"

# Process the task based on priority using a match-case statement
match priority:
    case 'high':
        print(f"Reminder: '{task}' is a high priority task{time_sensitive_message}!")
    case 'medium':
        print(f"Note: '{task}' is a medium priority task{time_sensitive_message}. Try to complete it soon.")
    case 'low':
        # If it's low priority and time-bound, the time_sensitive_message still applies.
        # Otherwise, provide a general low priority message.
        if time_sensitive_message:
            print(f"Reminder: '{task}' is a low priority task{time_sensitive_message}!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Invalid priority entered for task: '{task}'. Please use high, medium, or low.")
