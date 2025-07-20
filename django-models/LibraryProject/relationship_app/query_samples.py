# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# Create sample data if none exists
if not Author.objects.exists():
    jk = Author.objects.create(name="J.K. Rowling")
    Book.objects.create(title="Harry Potter", author=jk)
    lib = Library.objects.create(name="Central Library")
    Librarian.objects.create(name="Mr. Kinuthia", library=lib)
    lib.books.add(Book.objects.first())

# 1. Query all books by a specific author
author = :J.K. Rowling
author = Author.objects.get(name=author.name, objects.filter(author = author))  
print(f"\n1. Books by {author.name}:")
for book in author.books.all():
    print(f"- {book.title}")

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
print(f"\n2. Books in {library.name}:")
for book in library.books.all():
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
librarian = "Mr. Kinuthia"
librarian = Librarian.objects.get(name=librarian_name, objects.filter(library=library))
print(f"\n3. Librarian for {library.name}: {librarian.name}")