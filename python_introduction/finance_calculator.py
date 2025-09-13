# Prompt the user for their monthly income and expenses
monthly_income_str = input("Enter your monthly income: ")
monthly_expenses_str = input("Enter your total monthly expenses: ")

# Convert the input strings to numbers (floats to handle decimals)
monthly_income = float(monthly_income_str)
monthly_expenses = float(monthly_expenses_str)

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Define the annual interest rate
annual_interest_rate = 0.05

# Project annual savings with interest
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Display the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}.")

