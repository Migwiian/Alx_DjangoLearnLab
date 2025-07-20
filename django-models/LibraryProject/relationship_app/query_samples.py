# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

if not Author.objects.exists():
    jk = Author.objects.create(name="J.K. Rowling")
    Book.objects.create(title="Harry Potter", author=jk)
    
    central_library = Library.objects.create(name="Central Library")
    Librarian.objects.create(name="Mr. Kinuthia", library=central_library)
    
    harry_potter_book = Book.objects.get(title="Harry Potter")
    central_library.books.add(harry_potter_book)

print("\n1. Books by a specific author:")
author_name_to_find = "J.K. Rowling"
author_obj = Author.objects.get(name=author_name_to_find) 
books_by_author = Book.objects.filter(author=author_obj) 

print(f"   Books by {author_obj.name}:")
for book in books_by_author:
    print(f"   - {book.title}")

print("\n2. Books in a library:")
library_name_to_find = "Central Library"
library_obj = Library.objects.get(name=library_name_to_find)
print(f"   Books in {library_obj.name}:")
for book in library_obj.books.all():
    print(f"   - {book.title}")

print("\n3. Retrieve the librarian for a library:")
librarian_name_to_find = "Mr. Kinuthia" 
library_for_librarian_query = Library.objects.get(name="Central Library") 
librarian_obj = Librarian.objects.get(name=librarian_name_to_find, library=library_for_librarian_query)

print(f"   Librarian for {library_for_librarian_query.name}: {librarian_obj.name}")