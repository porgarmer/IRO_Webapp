from django.shortcuts import render
from management.models import *
# Create your views here.


def home(request):
    homepage = HomePageHero.objects.all().first()
    about_us = HomePageAboutUs.objects.first()
    stats = HomePageStats.objects.all()
    return render(request, "home.html", {
        "homepage": homepage,
        "about_us": about_us,
        "stats": stats,
    })
