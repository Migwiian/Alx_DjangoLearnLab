from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CommentForm, PostForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.db.models import Q

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ListPostsView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']  # Simpler than overriding get_queryset

class PostDetailView(View):
    model = Post  # No need for get_context_data - author is accessible via post.author in template
    

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    success_url = '/'  # Consider using reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    def get_success_url(self):
        return self.object.get_absolute_url() # Assuming you have a get_absolute_url method in your Post model

    def test_func(self):
        return self.request.user == self.get_object().author

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']  # Assuming post_id is passed in the URL
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()  # Redirect to the post detail page after creating comment
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'comment_form.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()  # Redirect to the post detail page after updating comment

    def test_func(self):
        return self.request.user == self.get_object().author    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author

class PostSearchView(ListView):
    model = Post
    template_name = 'blog/post_search.html'
    context_object_name = 'search_results'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # Search in title, content, and tags
            return Post.objects.filter(
                Qeturn Post.objects.filter(
                Q(title__icontains=query) |  
                Q(content__icontains=query) |  
                Q(tags__name__icontains=query) 
            ).distinct()
        return Post.objects.none()