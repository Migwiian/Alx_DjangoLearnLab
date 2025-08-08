# bookshelf/forms.py

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    A ModelForm for the Book model.
    It automatically generates form fields based on the Book model's fields.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']

class ExampleForm(forms.Form):
    # You can add form fields here
    name = forms.CharField(max_length=100)