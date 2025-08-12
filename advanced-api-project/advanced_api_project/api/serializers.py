from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    # This serializer converts the Book model into a format
    # that can be easily sent over an API, like JSON.
    # It also handles deserialization (converting incoming data back to a model).
    class Meta:
        model = Book
        fields = ['id', 'title', 'published_year', 'author']

    def validate_published_year(self, value):
        # We're adding a custom validation rule.
        # This function checks if the 'published_year' is in the future.
        current_year = date.today().year
        if value > current_year:
            # If the year is in the future, we raise a validation error.
            raise serializers.ValidationError("Published year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # This serializer converts the Author model into a JSON-friendly format.
    # It also shows the books associated with an author.
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']

# This is how the relationship between Author and Book is handled in the serializers:
# The 'books' field in the AuthorSerializer is a special field.
# We're telling the program to use the BookSerializer to process a list of books
# for each Author object. The 'many=True' tells it to expect a list of books,
# and 'read_only=True' means this data is for display only and can't be
# used to create or update books through the AuthorSerializer.
# This results in a nested structure where a GET request for an author
# will include all of their book data.