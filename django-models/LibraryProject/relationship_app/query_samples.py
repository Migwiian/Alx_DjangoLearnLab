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
for book in author.books.all():
    print(f"- {book.title}")

_ = Book.objects.filter(author=author)

library = Library.objects.first()
print(f"\n2. Books in {library.name}:")
for book in library.books.all():
    print(f"- {book.title}")

print(f"\n3. Librarian details for {library.name}:")
librarian = library.librarian
print(f"- Name: {librarian.name}")
print(f"- Library: {librarian.library.name}")
print(f"- Books under care: {library.books.count()}")