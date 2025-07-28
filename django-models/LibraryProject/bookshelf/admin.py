# bookshelf/admin.py

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the Django admin interface for the Book model.
    """
    list_display = ('title', 'author', 'publication_year') # Display these fields in the list view
    list_filter = ('publication_year', 'author') # Add filters for these fields
    search_fields = ('title', 'author') # Add search capability for these fields
    # Optional: Add a date hierarchy for publication_year if it were a DateField
    # date_hierarchy = 'publication_year'from django.contrib import admin

