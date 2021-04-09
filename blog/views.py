from django.shortcuts import render, get_object_or_404
from .models import Blog_post


def all_blog_posts(request):
    all_posts = Blog_post.objects.all()
    return render(request, 'blog/all.html',{'all_posts':all_posts})

def detail(request, blog_id):
    post = get_object_or_404(Blog_post, pk=blog_id)
    return render(request, 'blog/detail.html', {'post':post})