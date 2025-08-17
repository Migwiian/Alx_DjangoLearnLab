from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.ListPostsView.as_view(), name='post_list'),  # ✅ .as_view() added  
    path('posts/new/', views.CreatePostView.as_view(), name='post_new'),  
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  
    path('posts/<int:pk>/edit/', views.UpdatePostView.as_view(), name='post_edit'),  
    path('posts/<int:pk>/delete/', views.DeletePostView.as_view(), name='post_delete'),  

    
]