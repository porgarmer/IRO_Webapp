from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib import messages
from django.http import JsonResponse

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
    return render(request, 'accounts/login.html')

def admin_logout(request):
    logout(request)
    return redirect(reverse('management:login'))

@login_required()
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


"""home page functions"""
@login_required
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
 
@login_required
def news_articles(request):
    # Filter and search functionality
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    
    # Filtering the articles
    newsarticles = NewsArticle.objects.all().order_by('-created_at')
    
    if search_query:
        newsarticles = newsarticles.filter(title__icontains=search_query)
    
    if category_filter:
        newsarticles = newsarticles.filter(category__id=category_filter)
    
    # Add news or article
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            messages.success(request, 'Post added successfully.')
            return redirect('management:news_articles')
    
    categories = NewsArticleCategory.objects.all()
    form = NewsArticleForm()  # Include request.FILES for file uploads
    return render(request, 'news&articles/news&articles.html', {
        'form': form,
        'newsarticles': newsarticles,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter,
    })

@login_required
def edit_news_and_articles(request, slug):
    # Get the news article to edit based on the slug
    newsarticle = get_object_or_404(NewsArticle, slug=slug)
    
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES, instance=newsarticle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully.')
            return redirect('management:news_articles')
    else:
        form = NewsArticleForm(instance=newsarticle)
    
    return render(request, 'news&articles/edit_news_article.html', {
        'form': form,
        'newsarticle': newsarticle
    })

@login_required
def delete_news_article(request, slug):
    # Delete the article
    newsarticle = get_object_or_404(NewsArticle, slug=slug)
    newsarticle.delete()
    messages.success(request, 'Post deleted successfully.')
    return redirect('management:news_articles')

@login_required
def view_news_article(request, slug):
    # Get the specific news article to view based on the slug
    newsarticle = get_object_or_404(NewsArticle, slug=slug)
    
    return render(request, 'news&articles/view_news_article.html', {
        'newsarticle': newsarticle
    })

@login_required
def add_rescue(request):
    if request.method == 'POST':
        form = AdoptableRescueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rescue added successfully.')
            return redirect('management:adoptable_rescues')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AdoptableRescueForm()

    return render(request, 'adoptable_rescues/add_rescue.html', {'form': form})

# Existing view for adoptable rescues
def adoptable_rescues(request):
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')

    rescues = AdoptableRescue.objects.all()
    if search_query:
        rescues = rescues.filter(name__icontains=search_query)
    if category_filter:
        rescues = rescues.filter(category__id=category_filter)

    categories = RescueCategory.objects.all()

    return render(request, 'adoptable_rescues/adoptable_rescues.html', {
        'rescues': rescues,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter,
    })

@login_required
def edit_rescue(request, rescue_id):
    # Get the rescue object
    rescue = get_object_or_404(AdoptableRescue, id=rescue_id)

    # Get all categories to populate the dropdown
    categories = RescueCategory.objects.all()

    if request.method == 'POST':
        form = AdoptableRescueForm(request.POST, request.FILES, instance=rescue)
        if form.is_valid():
            form.save()
            return redirect('management:view_rescue', pk=rescue.id)  # Change rescue_id to pk
    else:
        form = AdoptableRescueForm(instance=rescue)

    return render(request, 'adoptable_rescues/edit_rescue.html', {
        'form': form,
        'rescue': rescue,
        'categories': categories,
    })


@login_required
def delete_rescue(request, pk):
    rescue = get_object_or_404(AdoptableRescue, pk=pk)
    rescue.delete()
    messages.success(request, 'Rescue deleted successfully.')
    return redirect('management:adoptable_rescues')

@login_required
def view_rescue(request, pk):
    rescue = get_object_or_404(AdoptableRescue, pk=pk)
    return render(request, 'adoptable_rescues/view_rescue.html', {'rescue': rescue})


def google_form_list(request):
    forms = GoogleForm.objects.all()
    return render(request, 'adoption_form/list.html', {'forms': forms})

def google_form_create(request):
    if request.method == 'POST':
        form = GoogleFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('management:google_form_list')
    else:
        form = GoogleFormForm()
    return render(request, 'adoption_form/view.html', {'form': form})

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

def google_form_delete(request, pk):
    gform = get_object_or_404(GoogleForm, pk=pk)
    if request.method == 'POST':
        gform.delete()
        return redirect('management:google_form_list')
    return render(request, 'adoption_form/delete.html', {'gform': gform})