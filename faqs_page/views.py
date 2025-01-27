from django.shortcuts import render
from management.models import Faq
from django.db.models import Q
# Create your views here.
def faqs_page(request):
    
    return render(request, 'faqs_page/faqs_homepage.html') 

def faqs_page(request):
    faqs = Faq.objects.all().order_by("-created_at")
    
    search_query = request.GET.get('search', '').strip()
    if search_query:
        faqs = faqs.filter(
            Q(title__icontains=search_query)|
            Q(description=search_query)
        )
    
    return render(request, 'faqs_page/faqs_homepage.html', {'faqs': faqs})