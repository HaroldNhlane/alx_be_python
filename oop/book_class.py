# book_class.py

class Book:
    """
    A class to represent a book with title, author, and publication year.
    It demonstrates the use of __init__, __del__, __str__, and __repr__ magic methods.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        The constructor method for the Book class.
        It initializes a new Book instance with the provided title, author, and year.
        Note: There is no print statement here to match the exact expected output.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        The destructor method for the Book class.
        This method is called when the object is about to be destroyed (deleted from memory).
        It prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        The informal string representation method for the Book class.
        This method is called by functions like print() and str().
        It should return a human-readable, concise string representation of the object.

        Returns:
            str: A formatted string: "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        The official string representation method for the Book class.
        This method is called by the repr() built-in function and by default in interactive
        interpreters. It should return a string that, if passed to eval(), would recreate
        the object, or at least a highly unambiguous representation.

        Returns:
            str: A string that can recreate the Book instance:
                 f"Book('{self.title}', '{self.author}', {self.year})".
        """
        # Using f-strings to construct the representation string.
        # Note the single quotes around title and author to ensure valid Python syntax
        # if the string were to be evaluated.
        return f"Book('{self.title}', '{self.author}', {self.year})"

