class Book:
    """
    Represents a book in the library system.

    Attributes:
        title (str): The public title of the book.
        author (str): The public author of the book.
        _is_checked_out (bool): Private attribute tracking availability.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False # Private attribute initialized to available

    def check_out(self):
        """Marks the book as checked out (unavailable)."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Returns the current availability status of the book."""
        return not self._is_checked_out

    def __str__(self):
        """Returns a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        # Private list to store all Book instances
        self._books = [] 

    def add_book(self, book):
        """
        Adds a new Book object to the library's collection.

        Args:
            book (Book): An instance of the Book class.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by title, if available.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {title}")
                return
        print(f"Error: '{title}' is not available or does not exist.")


    def return_book(self, title):
        """
        Returns a book by title, if it was checked out.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {title}")
                return
        print(f"Error: '{title}' was not checked out or does not exist.")


    def list_available_books(self):
        """
        Prints the title and author of all currently available books.
        """
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book) # Uses the Book's __str__ method
                available_count += 1

        if available_count == 0:
            print("No books are currently available.")

