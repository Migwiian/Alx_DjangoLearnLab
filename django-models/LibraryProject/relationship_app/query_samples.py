# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

if not Author.objects.exists():
    jk = Author.objects.create(name="J.K. Rowling")
    Book.objects.create(title="Harry Potter", author=jk)
    central_library = Library.objects.create(name="Central Library")
    Librarian.objects.create(name="Mr. Kinuthia", library=central_library)
    harry_potter_book = Book.objects.get(title="Harry Potter")
    central_library.books.add(harry_potter_book)

author_name = "J.K. Rowling" 
author_obj = Author.objects.get(name=author_name) 
books_by_author = Book.objects.filter(author=author_obj) 

print(f"Books by {author_obj.name}:")
for book in books_by_author:
    print(f"- {book.title}")

library_name = "Central Library" 
library_obj = Library.objects.get(name=library_name) 

print(f"Books in {library_obj.name}:")
for book in library_obj.books.all(): 
    print(f"- {book.title}")

librarian_name_to_find = "Mr. Kinuthia" 
library_for_librarian_query = Library.objects.get(name="Central Library") 

librarian_query_set = Librarian.objects.filter(name=librarian_name_to_find, library=library_for_librarian_query)
librarian_obj = librarian_query_set.first()

if librarian_obj:
    print(f"Librarian for {library_for_librarian_query.name}: {librarian_obj.name}")
else:
    print(f"No librarian named {librarian_name_to_find} found for {library_for_librarian_query.name}.")