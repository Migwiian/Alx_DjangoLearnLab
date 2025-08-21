from django.shortcuts import render
from rest_framework import viewsets, permissions, pagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.filters import SearchFilter


class PostCommentPagination(pagination.PageNumberPagination):
    """
    Custom pagination class for post and comment views.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
# Custom permission to only allow owners of an object to edit or delete it
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request.
        # This allows GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.author == request.user

# ViewSet for the Post model
class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `list`, `create`, `retrieve`,
    `update`, and `destroy` actions for the Post model.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = PostCommentPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        """
        Set the author of the post to the currently authenticated user
        when a new post is created.
        """
        serializer.save(author=self.request.user)

# ViewSet for the Comment model
class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `list`, `create`, `retrieve`,
    `update`, and `destroy` actions for the Comment model.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = PostCommentPagination

    def perform_create(self, serializer):
        """
        Set the author of the comment to the currently authenticated user
        when a new comment is created.
        """
        serializer.save(author=self.request.user)
