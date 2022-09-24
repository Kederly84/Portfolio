from django.shortcuts import render, get_object_or_404
from blogapp.models import Blog


def blog(request):
    blogs = Blog.objects.order_by('created_at')
    return render(request, 'blogapp/blog.html', {'blogs': blogs})


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    return render(request, 'blogapp/blog_detail.html', {'blog': blog})
