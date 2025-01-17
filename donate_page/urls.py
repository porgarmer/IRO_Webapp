from django.urls import path
from . import views

urlpatterns = [
    path("", views.donate, name="donate"), 
    path("shelter_wishlist/", views.shelter_wishlist, name="shelter_wishlist"), 
] 