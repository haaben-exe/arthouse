from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import CommentForm

from .models import Post, Comments

from django.http import HttpResponse



class LandingPage(LoginView):
    template_name = 'main/landing.html'

def HomePage(request):
    posts = Post.objects.all()
    return render(request, 'main/home.html', {'posts': posts})

class CreatePost(CreateView):
    model = Post
    template_name = 'form/postform.html'
    fields = ['title', 'image', 'category', 'description', 'tags']

def PostPage(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.all().order_by('-date')  # Show newest first

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user if request.user.is_authenticated else None
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'detail/post.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

class PostUpdate(UpdateView):
    model = Post
    template_name = 'form/postform.html'
    fields = '__all__'

class PostDelete(DeleteView):
    model = Post
    template_name = 'form/postdelete.html'
    success_url = '/home/'

def ProfilePage(request):
    return render(request, 'detail/profile.html')

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'form/login.html', {'form': form, 'error_message': 'Invalid login credentials. Please try again.'})
    else:
        form = AuthenticationForm()

    return render(request, 'form/login.html', {'form': form})

def Signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'form/signup.html', context)

def SearchPage(request):
    return HttpResponse('<h1>Henlo :3 is it me ur lookin fur??</h1>')


