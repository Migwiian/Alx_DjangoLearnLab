class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} (EBook, {self.file_size}MB)"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} (Print, {self.page_count} pages)"

class Library:
    def __init__(self, name="Default_lib"):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' by {book.author} added to {self.name}.")

    def list_books(self):
        print(f"\n--- Books in {self.name} ---")
        if not self.books:
            print("The library is empty.")
            return

        for book in self.books:
            print(f"- {book}")
