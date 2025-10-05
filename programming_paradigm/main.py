# Test script provided by the task
from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    # Note: The provided example output shows books added in a specific order
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    print("-" * 20)
    library.check_out_book("1984")
    print("-" * 20)
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    print("-" * 20)
    library.return_book("1984")
    print("-" * 20)
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

    # Additional tests (optional, but good practice)
    print("\n--- Additional Test Cases ---")
    library.check_out_book("The Catcher in the Rye") # Test non-existent book
    library.check_out_book("1984") # Check out again
    library.check_out_book("1984") # Check out already checked-out book

if __name__ == "__main__":
    main()
