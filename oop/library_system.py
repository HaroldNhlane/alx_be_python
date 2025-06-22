# library_system.py

class Book:
    """
    Base class for all books.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book object for display.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class for electronic books, inheriting from Book.
    Additional Attributes:
        file_size (int): The size of the e-book file in KB.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes a new EBook instance.
        Calls the base Book class's __init__ method and initializes file_size.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The file size of the e-book in kilobytes (KB).
        """
        super().__init__(title, author) # Call the constructor of the base class (Book)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook object, including file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class for print books, inheriting from Book.
    Additional Attributes:
        page_count (int): The number of pages in the print book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a new PrintBook instance.
        Calls the base Book class's __init__ method and initializes page_count.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        super().__init__(title, author) # Call the constructor of the base class (Book)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook object, including page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    A class representing a library, demonstrating composition.
    It manages a collection of Book, EBook, and PrintBook instances.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list to store books.
        """
        self.books = [] # This list will hold various book objects (composition)

    def add_book(self, book: Book):
        """
        Adds a book (can be Book, EBook, or PrintBook instance) to the library's collection.

        Args:
            book (Book): An instance of Book or any of its derived classes.
        """
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints the details of each book currently stored in the library.
        It utilizes the __str__ method of each book object to get its display string.
        """
        print("\n--- Books in the Library ---")
        if not self.books:
            print("The library is empty.")
            return

        for book in self.books:
            print(book) # This will automatically call the __str__ method of the book object
        print("----------------------------")