from django.shortcuts import render

# Create your views here.
def donate(request):
    
    return render(request, 'donate/donate.html') 

def in_kind_donations(request):
    
    return render(request, 'donate/in_kind_donations.html')

def adoption(request):
    
    return render(request, 'adoption/adoption.html') 