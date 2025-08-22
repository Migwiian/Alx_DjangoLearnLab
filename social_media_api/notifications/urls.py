from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.NotificationListView.as_view(), name='notification_list'),
]