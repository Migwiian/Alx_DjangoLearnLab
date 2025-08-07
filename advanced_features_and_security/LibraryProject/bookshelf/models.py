from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        """Create and save a regular user"""
        if not username:
            raise ValueError(_('Users must have a username'))
        email = self.normalize_email(email) if email else None
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """Create and save a superuser with minimal fields"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    """Custom user model with added fields"""
    date_of_birth = models.DateField(
        _('Date of Birth'), 
        blank=True, 
        null=True
    )
    profile_photo = models.ImageField(
        _('Profile Photo'),
        upload_to='profile_photos/',
        blank=True,
        null=True
    )
    
    objects = CustomUserManager()
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    
    class Meta:
        permissions  = [
            ("can_create_book", "Can create book"),
            ("can_view_book", "Can view book"),
            ("can_edit_book", "Can edit book"),
            ("can_delete_book", "Can delete book")
        ]
    