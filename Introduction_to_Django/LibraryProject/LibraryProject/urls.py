# LibraryProject/LibraryProject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView # Make sure this is imported if you're using LoginView explicitly
from bookshelf.views import SignUpView

urlpatterns = [
    path("admin/", admin.site.urls),

   
    path('accounts/', include('django.contrib.auth.urls')),

    
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'), # Corrected template name

    #Custom profile page - Corrected template path
    path('accounts/profile/',
         TemplateView.as_view(template_name='profile.html'), # CORRECTED template name
         name='profile'),

    #Custom signup page
    path("signup/", SignUpView.as_view(), name="signup"),

    path('bookshelf/', include('bookshelf.urls')),
]