# Prompt the user for a number
number_str = input("Enter a number to see its multiplication table: ")
number = int(number_str)

# Use a for loop to generate the multiplication table
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")

