from django.urls import path, include
from . import views
from .views import IsOwnerOrReadOnly, PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.get_feed, name='get_feed'),
    path('posts/<int:post_id>/like/', views.like_post, name='like_post'),
    path('posts/<int:post_id>/unlike/', views.unlike_post, name='unlike_post'),
    ]