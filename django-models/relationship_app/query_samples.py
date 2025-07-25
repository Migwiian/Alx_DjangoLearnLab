from relationship_app.models import Author, Book, Library, Librarian

if not Author.objects.exists():
    jk = Author.objects.create(name="J.K. Rowling")
    book = Book.objects.create(title="Harry Potter", author=jk)
    lib = Library.objects.create(name="Central Library")
    Librarian.objects.create(name="Ms. Smith", library=lib)
    lib.books.add(book)

author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
print(f"\n1. Books by {author.name}:")
books = Book.objects.filter(author=author)
for book in books:
    print(f"- {book.title}")

library_name = "Central Library"
library = Library.objects.get(name=library_name)
print(f"\n2. Books in {library.name}:")
for book in library.books.all():
    print(f"- {book.title}")

print(f"\n3. Librarian for {library.name}:")
librarian = Librarian.objects.get(library=library)
print(f"- {librarian.name}")