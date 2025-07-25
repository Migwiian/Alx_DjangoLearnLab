# relationship_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import Author, Book, Library, Librarian, UserProfile 
# --- Task 1: Admin View ---
def is_admin_group_member(user):
    return user.groups.filter(name='Admin').exists()


@login_required
@user_passes_test(is_admin_group_member, login_url='/accounts/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome to the Admin Dashboard!'})

# --- SignUp View (Task 2) ---
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        member_group, created = Group.objects.get_or_create(name='Member')
        self.object.groups.add(member_group)
        messages.success(self.request, 'Account created successfully! You are now a Member.')
        return response

# --- Task 0: Basic List Views (to satisfy your urls.py) ---

@login_required
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'relationship_app/author_list.html', {'authors': authors})

@login_required
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'relationship_app/author_detail.html', {'author': author})

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/book_detail.html', {'book': book})

@login_required
def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/library_list.html', {'libraries': libraries})

@login_required
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'relationship_app/library_detail.html', {'library': library})

@login_required
def librarian_list(request):
    librarians = Librarian.objects.all()
    return render(request, 'relationship_app/librarian_list.html', {'librarians': librarians})

@login_required
def librarian_detail(request, pk):
    librarian = get_object_or_404(Librarian, pk=pk)
    return render(request, 'relationship_app/librarian_detail.html', {'librarian': librarian})


@login_required
def app_home(request):
    return render(request, 'relationship_app/app_home.html')