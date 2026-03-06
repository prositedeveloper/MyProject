from django.shortcuts import render, get_object_or_404
from .models import News, Category

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'news/category.html', {
        'news': news,
        'category': category
    })