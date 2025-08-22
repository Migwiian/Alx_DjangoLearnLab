from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Notification model.
    Includes the username of the actor for easy display.
    """
    actor_username = serializers.CharField(source='actor.username', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'timestamp', 'is_read']
        read_only_fields = ['id', 'actor_username', 'verb', 'timestamp'] # is_read can be updated later