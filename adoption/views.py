from django.shortcuts import render
from management.models import AdoptableRescue
from django.db.models import Q

# Create your views here.
def adoption(request):
    adoptable_rescues = AdoptableRescue.objects.order_by('-date_added')
    
    search_query = request.GET.get('search', '').strip()
    if search_query:
        adoptable_rescues = adoptable_rescues.filter(
            Q(name__icontains=search_query)
        )
        
    selected_animal_type = request.GET.get('animal-type', '').strip()

    if selected_animal_type:
        adoptable_rescues = adoptable_rescues.filter(
            category__name__icontains=selected_animal_type
        )
        
    return render(request, 'adoption/adoption.html',{
        'adoptable_rescues': adoptable_rescues,
        'search_query': search_query,
        'selected_animal_type': selected_animal_type
    })