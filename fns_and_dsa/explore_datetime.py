from datetime import datetime, timedelta

def display_current_datetime():
    """
    Retrieves the current date and time and prints it in 
    'YYYY-MM-DD HH:MM:SS' format.
    """
    # Part 1: Display the Current Date and Time
    current_date = datetime.now()

    # Format the output as specified
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current date and time: {formatted_date}")

    # Return the current date object for use in the next function
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days and calculates the future date.

    Args:
        current_date (datetime): The starting datetime object.
    """
    # Part 2: Calculate a Future Date

    while True:
        try:
            # Prompt the user to enter an integer number of days
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number of days.")

    # Calculate the future date using timedelta
    time_delta = timedelta(days=days_to_add)
    future_date = current_date + time_delta

    # Format and print the future date in 'YYYY-MM-DD' format
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

    # Return the future_date variable as required by the prompt
    return future_date

def main():
    # Execute Part 1 and get the starting date
    current_date = display_current_datetime()

    # Execute Part 2 using the date from Part 1
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
