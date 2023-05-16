from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.all()

    return render(
    request,
    'todos/index.html',
    {
    'posts': posts,
    }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
    request,
    'todos/single_post_page.html',
    {
    'post': post,
    }
    )