from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post

def home(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    recent_posts = posts[:3]
    context = {
        'posts': posts,
        'recent_posts': recent_posts
    }
    print(context)
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")