from rest_framework import serializers
from models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn_number']
        read_only_fields = __all__  # Make all fields read-only by default