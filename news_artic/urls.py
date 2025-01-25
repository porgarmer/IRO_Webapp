from django.shortcuts import render
from . import views
from django.urls import path

app_name = 'news&articles'
# Create your views here.
urlpatterns = [
    path("", views.news_artic, name="news_articles"), 
    path('<slug:slug>/', views.news_artic_detail, name='news_artic_detail'),
] 