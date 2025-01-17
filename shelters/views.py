from django.shortcuts import render

# Create your views here.
def shelters(request):
    return render(request, 'shelters.html') 