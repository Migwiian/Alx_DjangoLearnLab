class Book:
    """
    Represents a single book with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title       # Public attribute for the book's title
        self.author = author     # Public attribute for the book's author
        self._is_checked_out = False # Private attribute to track availability, defaults to False (available)

    def check_out(self):
        """
        Marks the book as checked out if it's currently available.
        Returns True if successful, False otherwise (e.g., already checked out).
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as available (returned) if it's currently checked out.
        Returns True if successful, False otherwise (e.g., already available).
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Checks if the book is currently available (not checked out).
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        Used for printing the book's details, e.g., "Title by Author".
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book instances, allowing adding, checking out,
    returning, and listing available books.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = [] # Private list to store Book objects (encapsulation)

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): An instance of the Book class to add.
        """
        if isinstance(book, Book): # Basic validation to ensure a Book object is added
            self._books.append(book)
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title):
        """
        Finds a book by title and marks it as checked out if available.
        Prints a message if the book is not found or already checked out.

        Args:
            title (str): The title of the book to check out.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.check_out(): # Calls the Book object's method to change its status
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                break # Exit loop once book is found
        if not found:
            print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """
        Finds a book by title and marks it as available (returned).
        Prints a message if the book is not found or not currently checked out.

        Args:
            title (str): The title of the book to return.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.return_book(): # Calls the Book object's method to change its status
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                break # Exit loop once book is found
        if not found:
            print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """
        Prints the title and author of all books currently available (not checked out).
        If no books are available, prints a corresponding message.
        """
        available_found = False
        for book in self._books:
            if book.is_available(): # Uses the Book object's method to check availability
                print(book) # This uses the Book's __str__ method automatically
                available_found = True
        if not available_found:
            print("No books currently available.")
