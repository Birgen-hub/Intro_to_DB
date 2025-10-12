import sys

# Attempt to import the Book class
try:
    from book_class import Book
except ImportError:
    print("Error: Could not import Book class. Ensure book_class.py is present.")
    sys.exit(1)

def main():
    """
    Demonstrates the functionality of the Book class and its magic methods.
    """
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method (used by print())
    print(my_book)  

    # Demonstrating the __repr__ method (used by repr())
    print(repr(my_book)) 

    # Deleting a book instance to explicitly trigger __del__
    # This is guaranteed to trigger the destructor
    del my_book

    # Note: In a larger program, __del__ is called automatically when 
    # the reference count drops to zero, but explicit 'del' ensures it fires immediately.

if __name__ == "__main__":
    main()
