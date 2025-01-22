from django.shortcuts import render

# Create your views here.
def volunteer(request):
    
    return render(request, 'volunteer/volunteer.html')