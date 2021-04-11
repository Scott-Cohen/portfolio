from django.shortcuts import render

def all_blog_posts(request):
    return render(request, 'blog/all.html')
