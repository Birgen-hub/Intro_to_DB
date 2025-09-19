# Prompt the user for the size of the pattern
size_str = input("Enter the size of the pattern: ")

# Convert the input string to an integer
size = int(size_str)

# Use a while loop for the rows
row = 0
while row < size:
    # Use a for loop to print the asterisks for each column
    for _ in range(size):
        print("*", end="")

    # Print a newline after each row is complete
    print()

    # Increment the row counter
    row += 1

