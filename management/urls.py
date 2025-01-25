from django.urls import path
from . import views

app_name = 'management'
urlpatterns = [
    path('', views.admin_login, name='login'),
    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('homepage/hero-section', views.homepage_hero_section, name='homepage_hero_section'),
    path('news-articles', views.news_and_articles, name='news_articles'),
    path('edit-news&articles/<int:id>/', views.edit_news_and_articles, name='edit_news&articles'),

] 