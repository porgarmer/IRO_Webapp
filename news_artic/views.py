from django.shortcuts import render,  get_object_or_404
from management.models import NewsArticle

# Create your views here.
def news_artic(request):
     return render(request, 'news_artic.html') 


def news_artic_detail(request, slug):
     news_artic = get_object_or_404(NewsArticle   , slug=slug)
     return render(request, 'news_artic_detail.html',{
          'news_artic': news_artic,
     })
