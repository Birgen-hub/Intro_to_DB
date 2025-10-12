# Test script provided by the task
import sys

# Attempt to import the required classes
try:
    from library_system import Book, EBook, PrintBook, Library
except ImportError:
    print("Error: Could not import classes from library_system.py. Check file existence.")
    sys.exit(1)

def main():
    """
    Demonstrates adding different book types to the Library and listing them.
    """
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    # Assuming file size is in KB for the EBook output
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500) 
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    print("--- Adding Books ---")
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    print("\n--- Listing All Books ---")
    my_library.list_books()

if __name__ == "__main__":
    main()
