from django.shortcuts import render
from .models import Post

def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/feed.html', {'posts': posts})
