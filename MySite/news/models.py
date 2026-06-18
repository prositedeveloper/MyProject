from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def my_func(self):
        return "Последние новости"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})
    
    class Meta: 
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Comment(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    
    def __str__(self):
        return f'Комментарий от {self.author}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']