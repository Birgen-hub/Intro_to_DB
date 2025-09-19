# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task’s priority (high, medium, low)
priority = input("Priority (high/medium/low): ")

# Ask if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ")

# Use a variable to hold the reminder message
reminder = ""

# Process the task based on priority using a Match Case statement
match priority.lower():
    case "high":
        if time_bound.lower() == "yes":
            reminder = f"Reminder: {task} is a high priority task that requires immediate attention today!"
        else:
            reminder = f"Reminder: {task} is a high priority task."
    case "medium":
        reminder = f"Note: {task} is a medium priority task."
    case "low":
        if time_bound.lower() == "no":
            reminder = f"Note: {task} is a low priority task. Consider completing it when you have free time."
        else:
            reminder = f"Note: {task} is a low priority task."
    case _:
        reminder = f"Note: {task} has an unassigned priority."

# Print the final reminder
print(reminder)

