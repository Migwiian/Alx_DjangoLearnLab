from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Book, 
from .models import Library

def book_list(request):
    return render(
        request,
        'relationship_app/list_books.html',  # Exact template path
        {'books': Book.objects.all()}  # Exact queryset
    )

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'