from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

from django.http import HttpResponse

# class Post:
#     def __init__(self, title, category, description, tags):
#         self.title = title
#         self.category = category
#         self.description = description
#         self.tags = tags


def LandingPage(request):
    return render(request, 'main/landing.html')

def HomePage(request):
    posts = Post.objects.all()
    return render(request, 'main/home.html', {'posts': posts})

class CreatePost(CreateView):
    model = Post
    template_name = 'form/postform.html'
    fields = '__all__'

def PostPage(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'detail/post.html', {'post': post})

class PostUpdate(UpdateView):
    model = Post
    template_name = 'form/postform.html'
    fields = '__all__'

class PostDelete(DeleteView):
    model = Post
    success_url = '/cats/'

def ProfilePage(request):
    return render(request, 'detail/profile.html')

def SearchPage(request):
    return HttpResponse('<h1>Henlo :3 is it me ur lookin fur??</h1>')


