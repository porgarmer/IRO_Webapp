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
    path('add-news&articles', views.add_news_and_articles, name='add_news&articles'),
    path('edit-news&articles/<int:id>/', views.edit_news_and_articles, name='edit_news&articles'),
    path('delete-news&articles', views.delete_news_and_articles, name='delete_news&articles'),
    path('adoptable-rescues/', views.adoptable_rescues, name='adoptable_rescues'),
    path('add_rescue/', views.add_rescue, name='add_rescue'),
    path('adoptable-rescue/<int:rescue_id>/edit/', views.edit_rescue, name='edit_rescue'),
    path('adoptable-rescue/<int:pk>/delete/', views.delete_rescue, name='delete_rescue'),
    path('adoptable-rescue/<int:pk>/', views.view_rescue, name='view_rescue'),
    path('google-forms/', views.google_form_list, name='google_form_list'),
    path('google-forms/new/', views.google_form_create, name='google_form_create'),
    path('google-forms/<int:pk>/edit/', views.google_form_update, name='google_form_update'),
    path('google-forms/<int:pk>/delete/', views.google_form_delete, name='google_form_delete'),

] 