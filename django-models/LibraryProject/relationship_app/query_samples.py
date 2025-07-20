from relationship_app.models import Author, Book, Library, Librarian

# Create sample data if none exists
if not Author.objects.exists():
    jk = Author.objects.create(name="J.K. Rowling")
    book = Book.objects.create(title="Harry Potter", author=jk)
    lib = Library.objects.create(name="Central Library")
    Librarian.objects.create(name="Ms. Smith", library=lib)
    lib.books.add(book)

# 1. Query all books by a specific author (EXACT FORMAT REQUIRED)
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)  # First required pattern
print(f"\n1. Books by {author.name}:")
for book in Book.objects.filter(author=author):  # Second required pattern
    print(f"- {book.title}")

# 2. List all books in a library (EXACT FORMAT REQUIRED)
library_name = "Central Library"
library = library.objects.get(name=library_name)
print(f"\n2. Books in {library.name}:")
for book in library.books.all():
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
print(f"\n3. Librarian for {library.name}:")
librarian = Librarian.objects.get(library=library)
print(f"- {librarian.name}")