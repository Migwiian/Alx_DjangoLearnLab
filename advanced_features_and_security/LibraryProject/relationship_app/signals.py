from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver function to automatically create or update a UserProfile
    whenever a User object is saved.

    Args:
        sender: The model class that sent the signal (User in this case).
        instance: The actual instance of the User that was saved.
        created (bool): True if a new record was created, False if an existing record was updated.
        kwargs: Additional keyword arguments.
    """
    if created:
        # If a new User was just created, create a corresponding UserProfile.
        # The 'role' field will default to 'Member' as defined in your UserProfile model.
        UserProfile.objects.create(user=instance)
    else:
        # If an existing User was saved (not created), ensure its UserProfile is also saved.
        # This is important if you modify UserProfile fields directly and then save the User.
        # The hasattr check prevents errors if, for some reason, a User doesn't have a profile yet
        # (e.g., from old data or specific test setups before profiles were mandatory).
        if hasattr(instance, 'userprofile'):
            instance.userprofile.save()
        # else:
        #   If you reach here, it means an existing User was saved, but it somehow
        #   doesn't have a UserProfile. This is an edge case that usually indicates
        #   a data inconsistency. The 'create' logic handles new users, so for existing
        #   users without a profile, you might want to log an error or handle it
        #   differently depending on your application's requirements.
        #   For most cases, the 'if created' block ensures all new users get a profile.
