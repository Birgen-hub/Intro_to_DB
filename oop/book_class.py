class Book:
    """
    A Book class demonstrating the use of essential Python magic methods:
    __init__, __del__, __str__, and __repr__.
    """

    def __init__(self, title, author, year):
        """
        Constructor: Initializes a Book instance with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor: Called when the object is garbage collected.
        Prints a message showing the book being deleted.
        """
        # Prints the required message format
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation: Returns a user-friendly, readable string 
        for the book instance (used by print()).

        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Returns a string that could be used 
        to recreate the object (used by repr()).

        Format: f"Book('{self.title}', '{self.author}', {self.year})"
        """
        # Note the quotes around title and author, but not around year
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Note: No main function is needed here, as the class is imported by main.py
