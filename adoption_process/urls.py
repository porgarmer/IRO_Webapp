from django.urls import path
from . import views

urlpatterns = [
    path("", views.adoption_process, name="adoption_process"), 
    
] 