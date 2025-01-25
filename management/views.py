from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import (
    HomePageForm,
    NewsArticleForm,
    NewsArticle
    )
from .models import *
from django.contrib import messages


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

def table(request):
    return render(request, 'table/table.html')
