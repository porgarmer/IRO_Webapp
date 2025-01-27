from django.shortcuts import render
from . import views
from django.urls import path

app_name = 'resources'
# Create your views here.
urlpatterns = [
    path("", views.educ_reso, name="education_resources"), 
    path('<slug:slug>/', views.resource_detail, name='resource_detail'),

] 