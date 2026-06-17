from django.urls import path
from .views import NewsListView, ViewNews, NewsCreateView, CategoryDetailView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news-list/', NewsListView.as_view(), name='index'),
    path('news-list/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news-list/add/', NewsCreateView.as_view(), name='news_add'),
    path('news-list/category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:category_id>/', views.get_category, name='category'),
    path('<int:news_id>/', views.view_news, name='view_news'),
    path('add/', views.add_news, name='add_news'),
    path('comment/add/', views.add_comment, name='add_comment'),
]