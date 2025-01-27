from django.shortcuts import render
from management.models import HomePage, HomePageStats
# Create your views here.
def home(request):
    homepage = HomePage.objects.all().first()
    
    stats = HomePageStats.objects.all()
    return render(request, "home.html", {
        "homepage": homepage,
        "stats": stats,
    })