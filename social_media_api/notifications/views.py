from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    """
    API view for users to list their own notifications.
    """
    serializer_class = NotificationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view returns a list of all notifications for the currently authenticated user.
        It filters based on the recipient and orders by newest first.
        """
        # Get the notifications for the logged-in user
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')