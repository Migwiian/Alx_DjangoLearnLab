from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length = 500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True) # Image field for profile pictures
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)  # Many-to-many relationship for followers
    def __str__(self):
        return self.username