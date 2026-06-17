from django.shortcuts import render, redirect, get_object_or_404 
from .models import News, Category, Comment
from .forms import NewsForm, NewsModelForm, CommentForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView as BaseCreateView
from datetime import datetime
from django.urls import reverse_lazy

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

class NewsListView(ListView):
    model = News 
    template_name = 'news_list.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница новостей'
        context['current_time'] = datetime.now()
        return context 

    def get_queryset(self):
        return News.objects.filter(is_published=True)

class ViewNews(DetailView):
    model = News 
    context_object_name = 'news_item'

class NewsCreateView(BaseCreateView):
    model = News 
    form_class = NewsForm 
    template_name = 'news/news_add.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('instance', None)
        return kwargs
    
    def form_valid(self, form):
        news = News.objects.create(
            title=form.cleaned_data['title'],
            content=form.cleaned_data['content'],
            is_published=form.cleaned_data['is_published'],
            category=form.cleaned_data['category'],
        )
        return redirect(self.success_url)

class CategoryDetailView(DetailView):
    model = Category 
    template_name = 'news/category_detail.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = self.object.news_set.filter(is_published=True)
        return context