from django.shortcuts import render

# Create your views here.
def adoption(request):
    return render(request, 'adoption/adoption.html')