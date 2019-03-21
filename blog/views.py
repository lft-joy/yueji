from django.shortcuts import render
from .models import Blog


# Create your views here.


def blog_page(requests):
    blogs = Blog.objects
    return render(requests, 'blog.html', {'blogs': blogs})
