from django.urls import path
from . import views

urlpatterns = [
    path("", views.donate, name="donate"), 
    path("in-kind-donations/", views.in_kind_donations, name="in_kind_donations"), 
    
] 