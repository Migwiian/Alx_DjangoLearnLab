from django.urls import path
from .views import book_list, LibraryDetailView, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]