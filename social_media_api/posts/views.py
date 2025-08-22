from django.shortcuts import render
from rest_framework import generics, viewsets, permissions, pagination
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.filters import SearchFilter
from notifications.models import Notification


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


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, post_id):
    """
    Endpoint to like a post.
    """
    post = get_object_or_404(Post, id=post_id)
    if Like.objects.filter(user=request.user, post=post).exists():
        return Response(
            {"detail": "You have already liked this post."},
            status=status.HTTP_400_BAD_REQUEST
        )
    like = Like.objects.get_or_create(user=request.user, post=post)[0] #
    if request.user != post.author:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )
    serializer = LikeSerializer(like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, post_id):
    """
    Remove a like from a specific post.
    """
    # Get the post object or return 404
    post = generics.get_object_or_404(Post, id=post_id)
    
    # Try to get the like object
    like = generics.get_object_or_404(Like, user=request.user, post=post)
    
    # Delete the like
    like.delete()
    
    return Response(
        {"detail": "Post unliked successfully."},
        status=status.HTTP_200_OK
    )
