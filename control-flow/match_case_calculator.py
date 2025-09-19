# Prompt the user for two numbers
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Convert the input strings to floats
num1 = float(num1_str)
num2 = float(num2_str)

# Prompt for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Use match case to perform the calculation
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation.")

