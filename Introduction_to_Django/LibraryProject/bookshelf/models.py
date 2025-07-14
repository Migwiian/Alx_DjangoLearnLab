from django.db import models

# Create your models here.
# bookshelf/models.py

from django.db import models

class Book(models.Model):
    """
    Represents a book in the library system.
    Defines the fields (columns) that each book entry will have in the database.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField() # Stores the year as a whole number

    # Optional: Adding a __str__ method for better representation in admin/shell
    def __str__(self):
        """
        Returns a string representation of the Book object.
        This is what will be displayed in the Django admin and other places.
        """
        return f"{self.title} by {self.author} ({self.publication_year})"
