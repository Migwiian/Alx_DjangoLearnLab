# relationship_app/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')
    address = models.CharField(max_length=255, blank=True, null=True) # Added address as it's common for a library

    def __str__(self):
        return self.name

# UserProfile model
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.role})"


class Librarian(models.Model):
    # This links a Librarian entry directly to a UserProfile (and thus to a Django User)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='librarian_details')
    # A librarian is assigned to a specific library
    library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True, blank=True, related_name='librarians_assigned')
    # You can add other fields here specific to a librarian, if needed later (e.g., employee_id, hiring_date)

    def __str__(self):
        return f"Librarian: {self.user_profile.user.username} ({self.library.name if self.library else 'No Library'})"

# Signal to automatically create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Signal to save the UserProfile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()