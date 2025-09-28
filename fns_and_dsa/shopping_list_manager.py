def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list application."""
    shopping_list = []

    while True:
        display_menu()

