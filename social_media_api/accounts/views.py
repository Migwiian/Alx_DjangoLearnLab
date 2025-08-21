from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework import generics


# Create your views here.
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': serializer.data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data # This is the user object returned by the .validate() method
            # Get or create a token for the user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'message': 'Login successful'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowUserView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if request.user.username == username:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        target_user = get_object_or_404(get_user_model(), username=username)
        request.user.following.add(target_user)

        return Response({
            "message": f"You are now following {target_user.username}.",
            "following_count": request.user.following.count(),
            "followers_count": target_user.followers.count(),
        }, status=status.HTTP_200_OK)
class UnfollowUserView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def destroy(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if request.user.username == username:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        target_user = get_object_or_404(get_user_model(), username=username)
        request.user.following.remove(target_user)

        return Response({
            "message": f"You have unfollowed {target_user.username}.",
            "following_count": request.user.following.count(),
            "followers_count": target_user.followers.count(),
        }, status=status.HTTP_200_OK)