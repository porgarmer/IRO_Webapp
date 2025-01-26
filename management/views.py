from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings

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
@login_required()
def homepage_hero_section(request):
    homepage = HomePage.objects.all().first()
    if request.method == 'POST':
        form = HomePageForm(request.POST, request.FILES, instance=homepage)
        if form.is_valid():
            form.save()
            return render(request, 'homepage/hero_section.html', {'form': form})    
    else:
        form = HomePageForm(instance=homepage)
    return render(request, 'homepage/hero_section.html', {'form': form})

  
@login_required()
def news_and_articles(request):
            
    newsarticles = NewsArticle.objects.all().order_by('-created_at')
    form = NewsArticleForm()  # Include request.FILES for file uploads
    return render(request, 'news&articles/news&articles.html', {
        'form': form,
        'newsarticles': newsarticles,
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
