from django.shortcuts import render, get_object_or_404
from .models import Blog

def blogs(request):
    blog = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'blog':blog})

def detail(request, blog_id):
    b = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'b':b})
