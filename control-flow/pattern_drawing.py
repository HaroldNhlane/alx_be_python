# Prompt the user for the pattern size and convert directly to an integer
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer for the pattern size.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
    exit()

# Draw the pattern using a while loop for rows and a for loop for columns
row_count = 0
while row_count < size:
    for _ in range(size):  # The for loop iterates 'size' times to print 'size' asterisks
        print("*", end="")
    print()  # Print a newline character after each row
    row_count += 1