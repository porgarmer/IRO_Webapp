from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'management'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    # path('edit-account/', auth_views.PasswordChangeView.as_view(template_name='accounts/edit.html'), name='edit_account'),
    path('edit-account/', views.PasswordsChangeView.as_view(), name='edit_account'),
    path('edit-account-success/', views.edit_account_success, name='edit-account-success'),

    
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('homepage/hero-section', views.homepage_hero_section, name='homepage_hero_section'),
    path('homepage/stats', views.homepage_stats, name='homepage_stats'),
    path('homepage/add-stats', views.add_homepage_stats, name='add_homepage_stats'),
    path('homepage/edit-stats/<int:id>', views.edit_homepage_stats, name='edit_homepage_stats'),
    path('homepage/delete-stat', views.delete_homepage_stats, name='delete_homepage_stats'),

    path('wishlists', views.wishlists, name='wishlists'),
    path('add-wishlist', views.add_wishlist, name='add_wishlist'),
    path('edit-wishlist/<int:id>', views.edit_wishlist, name='edit_wishlist'),
    path('delete-wishlist', views.delete_wishlist, name='delete_wishlist'),


    path('educational-resources', views.educational_resources, name='educational_resources'),
    path('add-resource', views.add_resource, name='add_resource'),
    path('edit-resource/<int:id>/', views.edit_resource, name='edit_resource'),
    path('delete-resource', views.delete_resource, name='delete_resource'),
    
    path('category-education-resources', views.category_resources, name='category_resources'),
    path('add-category-education-resources', views.add_category_resources, name='add_category_resources'),
    path('edit-category-education-resources/<int:id>/', views.edit_category_resources, name='edit_category_resources'),
    path('delete-category-education-resources', views.delete_category_resources, name='delete_category_resources'),
    
    path('news-articles', views.news_and_articles, name='news_articles'),
    path('add-news&articles', views.add_news_and_articles, name='add_news&articles'),
    path('edit-news&articles/<int:id>/', views.edit_news_and_articles, name='edit_news&articles'),
    path('delete-news&articles', views.delete_news_and_articles, name='delete_news&articles'),
    
    path('category-news&articles', views.category_news_and_articles, name='category_news&articles'),
    path('add-category-news&articles', views.add_category_news_and_articles, name='add_category_news_and_articles'),
    path('edit-category-news&articles/<int:id>/', views.edit_category_news_and_articles, name='edit_category_news_and_articles'),
    path('delete-category-news&articles', views.delete_category_news_and_articles, name='delete_category_news_and_articles'),
    
    path('adoptable-rescues/', views.adoptable_rescues, name='adoptable_rescues'),
    path('add_rescue/', views.add_rescue, name='add_rescue'),
    path('adoptable-rescue/<int:rescue_id>/edit/', views.edit_rescue, name='edit_rescue'),
    path('adoptable-rescue/delete/', views.delete_rescue, name='delete_rescue'),
    path('adoptable-rescue/<int:pk>/', views.view_rescue, name='view_rescue'),
    
    path('google-forms/', views.google_form_list, name='google_form_list'),
    path('google-forms/new/', views.google_form_create, name='google_form_create'),
    path('google-forms/<int:pk>/edit/', views.google_form_update, name='google_form_update'),
    path('google-forms/<int:pk>/delete/', views.google_form_delete, name='google_form_delete'),
    
    path('faqs', views.faqs, name='faqs'),
    path('add-faqs', views.add_faqs, name='add_faqs'),
    path('edit-faqs/<int:id>', views.edit_faqs, name='edit_faqs'),
    path('delete-faqs', views.delete_faqs, name='delete_faqs'),

] 