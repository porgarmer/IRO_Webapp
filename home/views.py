from django.shortcuts import render
from management.models import HomePage
# Create your views here.
def home(request):
    homepage = HomePage.objects.all().first()
    print(homepage)
    return render(request, "home.html", {
        "homepage": homepage
    })