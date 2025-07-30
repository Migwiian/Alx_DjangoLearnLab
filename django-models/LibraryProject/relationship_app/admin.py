# relationship_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 


from .models import Author, Book, Library, Librarian, UserProfile

class UserProfileInline(admin.StackedInline):
    """
    Defines an inline admin interface for UserProfile.
    This allows UserProfile fields to be edited directly on the User admin page.
    'StackedInline' displays fields vertically, 'TabularInline' displays them horizontally.
    """
    model = UserProfile
    can_delete = False  
    verbose_name_plural = 'User Profile' 
    fk_name = 'user


class CustomUserAdmin(UserAdmin):
    """
    Custom UserAdmin class that extends Django's default UserAdmin.
    It includes the UserProfileInline, so UserProfile fields appear
    when managing User objects in the Django admin.

    We also customize list_display to show the 'role' directly in the User list.
    """
    inlines = (UserProfileInline,) 

 
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role')

    def get_role(self, obj):
        """
        Custom method to display the user's role from UserProfile in the User list view.
        Handles cases where a User might not yet have a UserProfile (though the signal
        should prevent this for new users).
        """
        try:
            return obj.userprofile.role
        except UserProfile.DoesNotExist:
            return "N/A (No Profile)"
    get_role.short_description = 'Role' 

admin.site.unregister(User)

admin.site.register(User, CustomUserAdmin)



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_count']
    search_fields = ['name']
    
    def book_count(self, obj):
        """Calculates the number of books written by the author."""
        return obj.books.count()
    book_count.short_description = 'Number of Books'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'library_count']
    list_filter = ['author']
    search_fields = ['title', 'author__name']
    
    def library_count(self, obj):
        """Counts how many libraries a book is available in."""
        return obj.libraries.count()
    library_count.short_description = 'Available in Libraries'

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_count', 'librarian_name']
    search_fields = ['name']
    
    def book_count(self, obj):
        """Calculates the number of books in a specific library."""
        return obj.books.count()
    book_count.short_description = 'Number of Books'
    
    def librarian_name(self, obj):
        """Retrieves the name of the librarian assigned to the library."""
        try:
            return obj.librarian.name
        except Librarian.DoesNotExist:
            return "No librarian assigned"
    librarian_name.short_description = 'Librarian'

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ['name', 'library']
    search_fields = ['name', 'library__name']
    list_filter = ['library']