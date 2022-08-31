from django.shortcuts import render
from blogapp.models import Blog


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blogapp/blog.html', {'blogs': blogs})
