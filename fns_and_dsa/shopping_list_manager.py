def display_menu():
    # This is the exact required print structure
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()

        # Simple input without stripping whitespace
        choice = input("Enter your choice: ") 

        if choice == '1':
            # 1. Add Item
            item_to_add = input("Enter the item to add: ")
            if item_to_add:
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' added to the list.")

        elif choice == '2':
            # 2. Remove Item
            if not shopping_list:
                print("The list is empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ")

            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            else:
                print(f"'{item_to_remove}' not found in the list.")

        elif choice == '3':
            # 3. View List
            if shopping_list:
                print("Current Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            # 4. Exit
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
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

