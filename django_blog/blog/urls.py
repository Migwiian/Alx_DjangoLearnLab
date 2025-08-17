from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.ListPostsView.as_view(), name='post_list'),  # ✅ .as_view() added  
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),  
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  
    path('post/<int:pk>/update/', views.UpdatePostView.as_view(), name='post_update'),  
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='post_delete'),  

    
]