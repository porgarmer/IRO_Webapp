from django.shortcuts import render

# Create your views here.
def donate(request):
    
    return render(request, 'donate/donate.html') 

def shelter_wishlist(request):
    
    return render(request, 'donate/shelter_wishlist.html') 