from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('articles', views.article_list, name='article-list'),
    path('articles/<int:article_id>/', views.article_detail, name='article-detail'),
]
