from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'post', 'author', 'content', 'created_at', 'updated_at')
class CommentSerializer(serializers.ModelSerializer):
    author = ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments')
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments')