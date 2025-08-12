from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/books/", ListView.as_view(), name="books-list"),
    path("api/books/<int:pk>/", DetailView.as_view(), name="books-detail"),
    path("api/books/create/", CreateView.as_view(), name="books-create"),
    path("api/books/<int:pk>/update/", UpdateView.as_view(), name="books-update"),
    path("api/books/<int:pk>/delete/", DeleteView.as_view(), name="books-delete"),
]