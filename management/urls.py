from django.urls import path
from . import views

app_name = 'management'
urlpatterns = [
    path('', views.admin_login, name='login'),
    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('homepage/hero-section', views.homepage_hero_section, name='homepage_hero_section'),
    path('news-articles/', views.news_articles, name='news_articles'),
    path('news-article/edit/<slug:slug>/', views.edit_news_and_articles, name='edit_news_article'),
    path('news-article/delete/<slug:slug>/', views.delete_news_article, name='delete_news_article'),
    path('news_article/<slug:slug>/', views.view_news_article, name='view_news_article'),

    path('table/', views.table, name='table'),

] 