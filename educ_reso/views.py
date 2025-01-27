from django.shortcuts import render,  get_object_or_404
from management.models import EducationalResource, ResourceCategory
from django.db.models import Q
# Create your views here.
def educ_reso(request):
     
     categories = ResourceCategory.objects.all().order_by('name')
     
     featured_post = EducationalResource.get_featured_posts(limit=1).first()
     latest_posts = EducationalResource.objects.filter(featured=False).order_by('-created_at')
     
     search_query = request.GET.get('search', '').strip()
     if search_query:
          latest_posts = latest_posts.filter(
               Q(title__icontains=search_query)|
               Q(summary__icontains=search_query)|
               Q(content__icontains=search_query)
          )
     
     select_category = request.GET.get('category', '').strip()
     if select_category:
          latest_posts = latest_posts.filter(
               Q(category__name__icontains=select_category)
          )
     
     
     return render(request, 'educ_reso.html', {
          'featured_post': featured_post,
          'latest_posts': latest_posts,
          'categories': categories,
          'search_query': search_query,
          'selected_category': select_category,
     }) 


def resource_detail(request, slug):
     latest_posts = EducationalResource.objects.order_by('-created_at').exclude(slug=slug)[:5]
     resource = get_object_or_404(EducationalResource, slug=slug)
     return render(request, 'educ_reso_detail.html',{
          'resource': resource,
          'latest_posts': latest_posts,
     })