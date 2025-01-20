from django.shortcuts import render

# Create your views here.
def adoption_process(request):
    
    return render(request, 'adoption_process/adoption_process.html')