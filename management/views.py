from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import (
    HomePageForm,
    NewsArticleForm,
    NewsArticle)
from .models import HomePage
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
