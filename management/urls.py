from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='management-login'),
    path('login/', views.admin_login, name='management-login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('homepage/hero-section', views.homepage_hero_section, name='homepage_hero_section')

] 