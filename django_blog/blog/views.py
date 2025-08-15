from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = Cu@stomUserCreationForm()
    return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home or login page after logout

@login_required
def profile(request):
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'user': request.user, 'posts': user_posts})
