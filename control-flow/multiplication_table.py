# Prompt the user to enter a number
number_str = input("Enter a number to see its multiplication table: ")

# Convert the input string to an integer
try:
    number = int(number_str)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Generate and print the multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, 11):  # Loop from 1 to 10 (inclusive)
    product = number * i
    print(f"{number} * {i} = {product}")