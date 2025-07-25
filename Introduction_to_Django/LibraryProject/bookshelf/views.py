from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test

def is_admin_group_member(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(is_admin_group_member, login_url='login')
def admin_view(request):
    return render(request, 'admin_view.html', {'message': 'Welcome to the admin view!'})

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"