# django-models/django-models/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView 
from relationship_app.views import SignUpView 

urlpatterns = [
    path("admin/", admin.site.urls),

    # Include the default auth URLs for login, logout, password management, etc.
    # This will automatically include URLs like /accounts/login/, /accounts/logout/, etc
    path('accounts/', include('django.contrib.auth.urls')),

    # Explicitly define /accounts/login/ to use your 'login.html' template
    path('accounts/login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Custom logout view to redirect after logout
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'), # <--- Added custom Logout for redirect

    # Custom profile page =
    path('accounts/profile/',
         TemplateView.as_view(template_name='relationship_app/profile.html'),
         name='profile'),

    # Your custom signup page
    path("signup/", SignUpView.as_view(), name="signup"),
    # Include the URLs from the relationship app
    path('relationship_app/', include('relationship_app.urls')),
]