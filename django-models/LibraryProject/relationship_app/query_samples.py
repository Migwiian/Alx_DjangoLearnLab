# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# Create sample data if none exists
if not Author.objects.exists():
    jk = Author.objects.create(name="J.K. Rowling")
    Book.objects.create(title="Harry Potter", author=jk)
    lib = Library.objects.create(name="Central Library")
    Librarian.objects.create(name="Ms. Smith", library=lib)
    lib.books.add(Book.objects.first())

# 1. Query all books by a specific author
author = Author.objects.first()
print(f"\n1. Books by {author.name}:")
for book in author.books.all():
    print(f"- {book.title}")

# 2. List all books in a library
library = Library.objects.first()
print(f"\n2. Books in {library.name}:")
for book in library.books.all():
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.first()
print(f"\n3. Librarian for {library.name}: {librarian.name}")