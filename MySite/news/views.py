from django.shortcuts import render, redirect, get_object_or_404 
from .models import News, Category, Comment
from .forms import NewsForm, NewsModelForm, CommentForm
from django.contrib import messages

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

def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {
        'news_item': news_item
    })

def add_news(request):
    if request.method == 'POST':
        form = NewsModelForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('view_news', news_id=news.pk)
    else:
        form = NewsForm()
    
    return render(request, 'news/add_news.html', {'form': form})


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.create(
                author=form.cleaned_data['author'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
            )

            messages.success(request, f'Спасибо, {comment.author}! Ваш комментарий добавлен!')
            return redirect('home')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = CommentForm()

    return render(request, 'news/add_comment.html', {'form': form})