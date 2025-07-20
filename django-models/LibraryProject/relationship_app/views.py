from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Book, 
from .models import Library

def book_list(request):
    return render(
        request,
        'relationship_app/list_books.html',
        {'books': Book.objects.all()}
    )

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'