class Book:
    """
    Base class representing a general book with a title and author.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation for generic Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book and adds file_size.
    """
    def __init__(self, title, author, file_size):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a string representation for EBook, including file size."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a physical print book.
    Inherits from Book and adds page_count.
    """
    def __init__(self, title, author, page_count):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns a string representation for PrintBook, including page count."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Class demonstrating composition, managing a collection of Book objects.
    """
    def __init__(self):
        # Composition: books attribute stores instances of Book, EBook, PrintBook
        self.books = [] 

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library's collection."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """Prints details of each book in the library using its __str__ method."""
        if not self.books:
            print("The library is empty.")
            return

        for book in self.books:
            # The appropriate __str__ method (from Book, EBook, or PrintBook)
            # is automatically called due to polymorphism.
            print(book)

