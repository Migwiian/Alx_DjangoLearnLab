from django.db import models

# Create your models here.
class Author(models.Model):
    # This model represents an author.
    # The 'name' field stores the author's full name.
    name = models.CharField(max_length=100)

    def __str__(self):
        # We're telling the program that for every Author object,
        # it should be represented by its name.
        return self.name

class Book(models.Model):
    # This model represents a book.
    title = models.CharField(max_length=200)
    # This field stores the year the book was published.
    publication_year = models.IntegerField()
    # This is a ForeignKey, linking each book to a specific Author.
    # The 'related_name' 'books' allows us to easily access
    # all books written by an author from the Author object.
    # The 'on_delete=models.CASCADE' means if an Author is deleted,
    # all of their books will also be deleted.
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        # We're telling the program that for every Book object,
        # it should be represented by its title.
        return self.title