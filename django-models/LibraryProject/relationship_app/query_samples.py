# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

if not Author.objects.exists():
    jk = Author.objects.create(name="J.K. Rowling")
    Book.objects.create(title="Harry Potter", author=jk)
    central_library = Library.objects.create(name="Central Library")
    Librarian.objects.create(name="Mr. Kinuthia", library=central_library)
    
    harry_potter_book = Book.objects.get(title="Harry Potter")
    central_library.books.add(harry_potter_book)

author = Author.objects.get(name="J.K. Rowling")
print(f"Books by {author.name}:")
for book in author.books.all():
    print(f"- {book.title}")

library_name = "Central Library"
library = Library.objects.get(name=library_name)
print(f"Books in {library.name}:")
for book in library.books.all():
    print(f"- {book.title}")

librarian_name = "Mr. Kinuthia"
librarian = Librarian.objects.get(name=librarian_name, library=library)
print(f"Librarian for {library.name}: {librarian.name}")