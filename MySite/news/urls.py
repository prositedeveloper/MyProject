from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:category_id>/', views.get_category, name='category'),
    path('<int:news_id>/', views.view_news, name='view_news'),
    path('add/', views.add_news, name='add_news'),
    path('comment/add/', views.add_comment, name='add_comment'),
]