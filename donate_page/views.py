from django.shortcuts import render
from management.models import Wishlist


def donate(request):
    return render(request, 'donate/donate.html') 

def in_kind_donations(request):
    wishlists = Wishlist.objects.order_by('-created_at')
    
    return render(request, 'donate/in_kind_donations.html',{
        'wishlists': wishlists
    })
