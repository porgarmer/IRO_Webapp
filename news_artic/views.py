from django.shortcuts import render,  get_object_or_404
from management.models import NewsArticle, NewsArticleCategory

# Create your views here.
def news_artic(request):
     
     categories = NewsArticleCategory.objects.all().order_by('name')
     
     featured_post = NewsArticle.get_featured_posts(limit=1).first()
     latest_posts = NewsArticle.objects.filter(featured=False).order_by('-created_at')
     return render(request, 'news_artic.html', {
          'featured_post': featured_post,
          'latest_posts': latest_posts,
          'categories': categories,
     }) 


def news_artic_detail(request, slug):
     latest_posts = NewsArticle.objects.order_by('-created_at').exclude(slug=slug)[:5]
     news_artic = get_object_or_404(NewsArticle, slug=slug)
     return render(request, 'news_artic_detail.html',{
          'news_artic': news_artic,
          'latest_posts': latest_posts,
     })
