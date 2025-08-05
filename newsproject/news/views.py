from django.shortcuts import render
from .models import News

def home(request):
    category = request.GET.get('category', 'top')
    news_list = News.objects.filter(category=category).order_by('-created_at')
    return render(request, 'news/home.html', {'news_list': news_list, 'category': category})
