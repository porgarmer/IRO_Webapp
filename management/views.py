from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from django.db.utils import IntegrityError
from django.db.models import Q
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect(reverse('management:dashboard'))
        else:
            messages.error(request, "Wrong username or password.")
            
    if request.user.is_authenticated:
        return redirect(reverse('management:dashboard'))
    return render(request, 'accounts/login.html')

def admin_logout(request):
    logout(request)
    return redirect(reverse('management:login'))


class PasswordsChangeView(PasswordChangeView):
    form_class = EditUserForm
    template_name='accounts/edit.html'
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('management:edit-account-success')

def edit_account_success(request):
    return render(request, 'accounts/edit_success.html')
    

@login_required()
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


# Home page functions
@login_required()
def homepage_hero_section(request):
    homepage = HomePage.objects.first()
    if request.method == 'POST':
        form = HomePageForm(request.POST, request.FILES, instance=homepage)
        if form.is_valid():
            form.save()
            return redirect('management:homepage_hero_section')  # Redirect to avoid resubmission
    else:
        form = HomePageForm(instance=homepage)
    return render(request, 'homepage/hero_section.html', {'form': form})

@login_required()
def homepage_stats(request):
    
    stats = HomePageStats.objects.all().order_by('-created_at')
    
    search_query = request.GET.get('search', '').strip()
    if search_query:
        stats = stats.filter(
            Q(name__icontains=search_query)|
            Q(number__icontains=search_query)
        )
        
    datesorted = request.GET.get('date-sort', '').strip()
    if datesorted == 'ascending':
        stats = stats.order_by('created_at')
    
    return render(request, 'homepage/stats_section/stats_section.html', {
        'stats': stats,
        'search_query': search_query,
        'datesorted': datesorted,
    })
    
@login_required()
def add_homepage_stats(request):
    if request.method == 'POST':
        form = HomePageStatsForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            stat = form.save()
            messages.success(request, 'Stat added successfully!')
            return redirect(reverse('management:homepage_stats'))

    form = HomePageStatsForm()

    return render(request, 'homepage/stats_section/add_stats.html', {
        'form': form,
    })    
    
@login_required()
def edit_homepage_stats(request, id):
    if request.method == 'POST':
        stat = get_object_or_404(HomePageStats, id=id)
        form = HomePageStatsForm(request.POST, request.FILES, instance=stat)  # Include request.FILES for file uploads
        if form.is_valid():
            stat = form.save()
            messages.success(request, 'Stat edited successfully!')
            return redirect(reverse('management:homepage_stats'))

    stat = get_object_or_404(HomePageStats, id=id)
    form = HomePageStatsForm(instance=stat)

    return render(request, 'homepage/stats_section/edit_stats.html', {
        'form': form,
        'stat': stat,
    })    
    
@login_required()
def delete_homepage_stats(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_ids')
        for i in selected_ids:
            selected_ids= i.split(',')
            
        HomePageStats.objects.filter(id__in=selected_ids).delete()
        
        if  len(selected_ids) > 1:
            messages.success(request, 'Stats deleted successfully')
        else:
            messages.success(request, 'Stat deleted successfully')
        return redirect(reverse('management:homepage_stats'))

    
# FAQs Functions
@login_required()
def wishlists(request):
    
    wishlists = Wishlist.objects.all().order_by('-created_at')
    
    search_query = request.GET.get('search', '').strip()
    if search_query:
        wishlists =wishlists.filter(
            Q(name__icontains=search_query)|
            Q(description__icontains=search_query)
        )
    
    datesorted = request.GET.get('date-sort', '').strip()
    if datesorted == 'ascending':
        wishlists = wishlists.order_by('created_at')
        
    return render (request, 'in_kind_donation/wishlists.html', {
        'wishlists': wishlists,
        'search_query': search_query,
        'datesorted': datesorted
    })

@login_required()
def add_wishlist(request):
    
    if request.method == "POST":
        form = WishlistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect(reverse('management:wishlists'))
        else:
            # If the form is invalid, display the error message from `form.errors`
            if 'name' in form.errors:
                messages.error(request, 'Wishlist already exists.')
            else:
                messages.error(request, 'Error adding wishlit.')
                
    form = WishlistForm()
    return render (request, 'in_kind_donation/add_wishlist.html', {
        'form': form
    })
    
@login_required()
def edit_wishlist(request, id):
    
    if request.method == "POST":
        wishlist = get_object_or_404(Wishlist, id=id)
        form = WishlistForm(request.POST, request.FILES, instance=wishlist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wishlist edited successfully.')
            return redirect(reverse('management:wishlists'))
        else:
            # If the form is invalid, display the error message from `form.errors`
            if 'name' in form.errors:
                messages.error(request, 'Wishlist already exists.')
            else:
                messages.error(request, 'Error adding wishlit.')
                
    wishlist = Wishlist.objects.get(id=id)
    form = WishlistForm(instance=wishlist)
    return render (request, 'in_kind_donation/edit_wishlist.html', {
        'form': form,
        'wishlist': wishlist,
    })
    
    
@login_required()
def delete_wishlist(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_ids')
        print(selected_ids)
        for i in selected_ids:
            selected_ids= i.split(',')
            
        Wishlist.objects.filter(id__in=selected_ids).delete()
        
        if  len(selected_ids) > 1:
            messages.success(request, 'Wishlists deleted successfully')
        else:
            messages.success(request, 'Wishlist deleted successfully')
        return redirect(reverse('management:wishlists'))

    
# Educational Resources functions
@login_required()
def educational_resources(request):
    
    resources = EducationalResource.objects.all().order_by('-created_at')
    categories = ResourceCategory.objects.all().order_by('name')
    
    search_query = request.GET.get('search', '').strip()
    if search_query:
        resources = resources.filter(
            Q(id__icontains=search_query)|
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )
        
    datesorted = request.GET.get('date-sort', '').strip()
    if datesorted == 'ascending':
        resources = resources.order_by('created_at')
    
    category_filter = request.GET.get('category', '').strip()
    print(category_filter)
    if category_filter:
        category = categories.get(name=category_filter)
        resources = EducationalResource.objects.filter(
            category=category
        )
        
    return render(request, 'educational_resources/resources.html', {
        'resources': resources,
        'search_query': search_query,
        'categories': categories,
        'datesorted': datesorted,
        'category_filter': category_filter,
    })
    
    
@login_required()
def add_resource(request):
    if request.method == 'POST':
        form = EducationalResourceForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            news_article = form.save()
            messages.success(request, 'Post added successfully!')
            return redirect(reverse('management:educational_resources'))

    form = EducationalResourceForm()

    return render(request, 'educational_resources/add_resource.html', {
        'form': form,
    })    
    
@login_required()
def edit_resource(request, id):
    if request.method == 'POST':
        resource = get_object_or_404(EducationalResource, id=id)
        form = EducationalResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post edited successfully.')
            return redirect(reverse('management:educational_resources'))

    resource = EducationalResource.objects.get(id=id)
    form = EducationalResourceForm(instance=resource)

    return render(request, 'educational_resources/edit_resource.html', {
        'form': form,
        'resource': resource
    })

@login_required()
def delete_resource(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_ids')
        for i in selected_ids:
            selected_ids= i.split(',')
            
        EducationalResource.objects.filter(id__in=selected_ids).delete()
        
        if  len(selected_ids) > 1:
            messages.success(request, 'Posts deleted successfully')
        else:
            messages.success(request, 'Post deleted successfully')
        return redirect(reverse('management:educational_resources'))


# Educational Resources Category page functions
@login_required()
def category_resources(request):
    
    categories = ResourceCategory.objects.all().order_by('name')
    
    search_query = request.GET.get('search', '').strip()
    if search_query:
        categories =categories.filter(
            Q(name__icontains=search_query)
        )
    
    namesorted = request.GET.get('name-sort', '').strip()
    if namesorted == 'descending':
        categories = categories.order_by('-name')
        
    return render (request, 'educational_resources/category/category_resources.html', {
        'categories': categories,
        'search_query': search_query,
        'namesorted': namesorted
    })
    
@login_required()
def add_category_resources(request):
    
    if request.method == "POST":
        form = ResourceCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect(reverse('management:category_resources'))
        else:
            # If the form is invalid, display the error message from `form.errors`
            if 'name' in form.errors:
                messages.error(request, 'Category already exists.')
            else:
                messages.error(request, 'Error adding exists.')
    form = ResourceCategoryForm()
    return render (request, 'educational_resources/category/add_category_resources.html', {
        'form': form
    })
    
@login_required()
def edit_category_resources(request, id):
    
    if request.method == "POST":
        resource_category = get_object_or_404(ResourceCategory, id=id)
        form = ResourceCategoryForm(request.POST, instance=resource_category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category edited successfully.')
            return redirect(reverse('management:category_resources'))
        else:
            # If the form is invalid, display the error message from `form.errors`
            if 'name' in form.errors:
                messages.error(request, 'Category already exists.')
            else:
                messages.error(request, 'Error adding exists.')
                
    resource_category = ResourceCategory.objects.get(id=id)
    form = ResourceCategoryForm(instance=resource_category)
    return render (request, 'educational_resources/category/edit_category_resources.html', {
        'form': form,
    })
    
@login_required()
def delete_category_resources(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_ids')
        print(selected_ids)
        for i in selected_ids:
            selected_ids= i.split(',')
            
        ResourceCategory.objects.filter(id__in=selected_ids).delete()
        
        if  len(selected_ids) > 1:
            messages.success(request, 'Categories deleted successfully')
        else:
            messages.success(request, 'Category deleted successfully')
        return redirect(reverse('management:category_resources'))    
    

# News&Articles page functions
@login_required()
def news_and_articles(request):
    
    newsarticles = NewsArticle.objects.all().order_by('-created_at')
    categories = NewsArticleCategory.objects.all().order_by('name')

    search_query = request.GET.get('search', '').strip()
    if search_query:
        newsarticles = newsarticles.filter(
            Q(id__icontains=search_query)|
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )
        
    datesorted = request.GET.get('date-sort', '').strip()
    if datesorted == 'ascending':
        newsarticles = newsarticles.order_by('created_at')
    
    category_filter = request.GET.get('category', '').strip()
    print(category_filter)
    if category_filter:
        category = NewsArticleCategory.objects.get(name=category_filter)
        newsarticles = NewsArticle.objects.filter(
            category=category
        )
    return render(request, 'news&articles/news&articles.html', {
        'newsarticles': newsarticles,
        'search_query': search_query,
        'categories': categories,
        'datesorted': datesorted,
        'category_filter': category_filter,
    })

@login_required()
def add_news_and_articles(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            news_article = form.save()
            messages.success(request, 'Post added successfully!')
            return redirect(reverse('management:news_articles'))
      
    form = NewsArticleForm()

    return render(request, 'news&articles/add_news&articles.html', {
        'form': form,
    })    

@login_required()
def edit_news_and_articles(request, id):
    if request.method == 'POST':
        news_article = get_object_or_404(NewsArticle, id=id)
        form = NewsArticleForm(request.POST, request.FILES, instance=news_article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post edited successfully.')
            return redirect(reverse('management:news_articles'))

    news_article = NewsArticle.objects.get(id=id)
    form = NewsArticleForm(instance=news_article)

    return render(request, 'news&articles/edit_news&articles.html', {
        'form': form,
        'news_article': news_article
    })

@login_required()
def delete_news_and_articles(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_ids')
        for i in selected_ids:
            selected_ids= i.split(',')
            
        NewsArticle.objects.filter(id__in=selected_ids).delete()
        
        if  len(selected_ids) > 1:
            messages.success(request, 'Posts deleted successfully')
        else:
            messages.success(request, 'Post deleted successfully')
        return redirect(reverse('management:news_articles'))


# News&Articles Category page functions
@login_required()
def category_news_and_articles(request):
    
    categories = NewsArticleCategory.objects.all().order_by('name')
    
    search_query = request.GET.get('search', '').strip()
    if search_query:
        categories =categories.filter(
            Q(name__icontains=search_query)
        )
    
    namesorted = request.GET.get('name-sort', '').strip()
    if namesorted == 'descending':
        categories = categories.order_by('-name')
        
    return render (request, 'news&articles/category/category_news&articles.html', {
        'categories': categories,
        'search_query': search_query,
        'namesorted': namesorted
    })

@login_required()
def add_category_news_and_articles(request):
    
    if request.method == "POST":
        form = NewsArticleCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect(reverse('management:category_news&articles'))
        else:
            # If the form is invalid, display the error message from `form.errors`
            if 'name' in form.errors:
                messages.error(request, 'Category already exists.')
            else:
                messages.error(request, 'Error adding exists.')

    form = NewsArticleCategoryForm()
    return render (request, 'news&articles/category/add_category_news&articles.html', {
        'form': form
    })
    
@login_required()
def edit_category_news_and_articles(request, id):
    
    if request.method == "POST":
        news_article_category = get_object_or_404(NewsArticleCategory, id=id)
        form = NewsArticleCategoryForm(request.POST, instance=news_article_category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category edited successfully.')
            return redirect(reverse('management:category_news&articles'))
        else:
            # If the form is invalid, display the error message from `form.errors`
            if 'name' in form.errors:
                messages.error(request, 'Category already exists.')
            else:
                messages.error(request, 'Error adding exists.')
                
    news_article_category = NewsArticleCategory.objects.get(id=id)
    form = NewsArticleCategoryForm(instance=news_article_category)
    return render (request, 'news&articles/category/edit_category_news&articles.html', {
        'form': form,
    })
    
@login_required()
def delete_category_news_and_articles(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_ids')
        print(selected_ids)
        for i in selected_ids:
            selected_ids= i.split(',')
            
        NewsArticleCategory.objects.filter(id__in=selected_ids).delete()
        
        if  len(selected_ids) > 1:
            messages.success(request, 'Categories deleted successfully')
        else:
            messages.success(request, 'Category deleted successfully')
        return redirect(reverse('management:category_news&articles'))


# Adoptable rescues functions
@login_required()
def add_rescue(request):
    if request.method == 'POST':
        form = AdoptableRescueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rescue added successfully.')
            return redirect('management:adoptable_rescues')
        else:
            if 'name' in form.errors:
                messages.error(request, 'Rescue already exists.')
            else:
                messages.error(request, 'Error adding rescue.')
            
    form = AdoptableRescueForm()
    return render(request, 'adoptable_rescues/add_rescue.html', {'form': form})

@login_required()
# Existing view for adoptable rescues
def adoptable_rescues(request):
    search_query = request.GET.get('search', '').strip()
    categories = RescueCategory.objects.all()

    rescues = AdoptableRescue.objects.all().order_by('-date_added')
    if search_query:
        rescues = rescues.filter(
                Q(name__icontains=search_query)|
                Q(category__name__icontains=search_query)|
                Q(description__icontains=search_query)
            )
        
    category_filter = request.GET.get('category', '').strip()
    if category_filter:
        rescues = rescues.filter(category__name=category_filter)
        
    datesorted =  request.GET.get('date-sort', '')
    if datesorted == 'ascending':
        rescues = rescues.order_by('date_added')
        
    namesorted =  request.GET.get('name-sort', '')
    if namesorted == 'ascending':
        rescues = rescues.order_by('name')
    elif namesorted == 'descending':
        rescues = rescues.order_by('-name')

    return render(request, 'adoptable_rescues/adoptable_rescues.html', {
        'rescues': rescues,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter,
        'datesorted': datesorted,
        'namesorted': namesorted,
    })

@login_required()
def edit_rescue(request, rescue_id):

    # Get all categories to populate the dropdown
    categories = RescueCategory.objects.all()

    if request.method == 'POST':
        rescue = get_object_or_404(AdoptableRescue, id=rescue_id)
        form = AdoptableRescueForm(request.POST, request.FILES, instance=rescue)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rescue edited successfully.')
            return redirect('management:adoptable_rescues')  # Change rescue_id to pk
        else:
            messages.error(request, 'Error editing rescue.')
    
    rescue = get_object_or_404(AdoptableRescue, id=rescue_id)
    form = AdoptableRescueForm(instance=rescue)

    return render(request, 'adoptable_rescues/edit_rescue.html', {
        'form': form,
        'rescue': rescue,
        'categories': categories,
    })


@login_required()
def delete_rescue(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_ids')
        for i in selected_ids:
            selected_ids= i.split(',')
            
        AdoptableRescue.objects.filter(id__in=selected_ids).delete()
        
        if  len(selected_ids) > 1:
            messages.success(request, 'Rescue removed successfully')
        else:
            messages.success(request, 'Rescues removed successfully')
        return redirect(reverse('management:adoptable_rescues'))
    
@login_required()
def view_rescue(request, pk):
    rescue = get_object_or_404(AdoptableRescue, pk=pk)
    return render(request, 'adoptable_rescues/view_rescue.html', {'rescue': rescue})

@login_required()
def google_form_list(request):
    forms = GoogleForm.objects.all()
    return render(request, 'adoption_form/list.html', {'forms': forms})

@login_required()
def google_form_create(request):
    if request.method == 'POST':
        form = GoogleFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('management:google_form_list')
    else:
        form = GoogleFormForm()
    return render(request, 'adoption_form/view.html', {'form': form})

@login_required()
def google_form_update(request, pk):
    gform = get_object_or_404(GoogleForm, pk=pk)
    if request.method == 'POST':
        form = GoogleFormForm(request.POST, instance=gform)
        if form.is_valid():
            form.save()
            return redirect('management:google_form_list')
    else:
        form = GoogleFormForm(instance=gform)
    return render(request, 'adoption_form/view.html', {'form': form})

@login_required()
def google_form_delete(request, pk):
    gform = get_object_or_404(GoogleForm, pk=pk)
    if request.method == 'POST':
        gform.delete()
        return redirect('management:google_form_list')
    return render(request, 'adoption_form/delete.html', {'gform': gform})


# FAQs Functions
@login_required()
def faqs(request):
    
    faq_objs = Faq.objects.all().order_by('-created_at')
    
    search_query = request.GET.get('search', '').strip()
    if search_query:
        faq_objs =faq_objs.filter(
            Q(title__icontains=search_query)|
            Q(description__icontains=search_query)
        )
    
    datesorted = request.GET.get('date-sort', '').strip()
    if datesorted == 'ascending':
        faq_objs = faq_objs.order_by('created_at')
        
    return render (request, 'faqs/faqs.html', {
        'faq_objs': faq_objs,
        'search_query': search_query,
        'datesorted': datesorted
    })

@login_required()
def add_faqs(request):
    
    if request.method == "POST":
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect(reverse('management:faqs'))
        else:
            # If the form is invalid, display the error message from `form.errors`
            if 'title' in form.errors:
                messages.error(request, 'Question already exists.')
            else:
                messages.error(request, 'Error adding faq.')

    form = FaqForm()
    return render (request, 'faqs/add_faq.html', {
        'form': form
    })
    
@login_required()
def edit_faqs(request, id):
    
    if request.method == "POST":
        faq = get_object_or_404(Faq, id=id)
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question edited successfully.')
            return redirect(reverse('management:faqs'))
        else:
            # If the form is invalid, display the error message from `form.errors`
            if 'title' in form.errors:
                messages.error(request, 'Question already exists.')
            else:
                messages.error(request, 'Error adding faq.')
                
    faq = Faq.objects.get(id=id)
    form = FaqForm(instance=faq)
    return render (request, 'faqs/edit_faq.html', {
        'form': form,
    })
    
@login_required()
def delete_faqs(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_ids')
        print(selected_ids)
        for i in selected_ids:
            selected_ids= i.split(',')
            
        Faq.objects.filter(id__in=selected_ids).delete()
        
        if  len(selected_ids) > 1:
            messages.success(request, 'Questions deleted successfully')
        else:
            messages.success(request, 'Question deleted successfully')
        return redirect(reverse('management:faqs'))
