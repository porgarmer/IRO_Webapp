from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from datetime import datetime
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

# Create your models here.
class HomePage(models.Model):
    #hero section fields
    hero_section_bg_photo = models.ImageField(null=True, blank=True, upload_to='homepage/')
    hero_section_title = CKEditor5Field(blank=True, null=True, config_name='extends')
    hero_section_subtitle = CKEditor5Field(blank=True, null=True, config_name='extends')
    hero_section_cta_btn_text = CKEditor5Field(blank=True, null=True, config_name='extends')
    
    #about us section fields
    about_us_section_photo = models.ImageField(null=True, blank=True, upload_to='about_us/')
    about_us_section_header = CKEditor5Field(blank=True, null=True, config_name='extends')
    about_us_section_content = CKEditor5Field(blank=True, null=True, config_name='extends')

class NewsArticleCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
class NewsArticle(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='news&articles/')
    featured = models.BooleanField(default=False)  # New field for featured posts

    # author =  # to be added
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(NewsArticleCategory, null=True, blank=True, related_name='news_article', on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    summary = CKEditor5Field(blank=True, null=True, config_name='extends')
    content = CKEditor5Field(blank=True, null=True, config_name='extends')
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
        if self.pk:
            old_file = NewsArticle.objects.get(pk=self.pk).photo
            if old_file and old_file != self.photo and os.path.isfile(old_file.path):
                os.remove(old_file.path)    
        super().save(*args, **kwargs)
        
        
    @staticmethod
    def get_featured_posts(limit=1):
        """Get the latest featured posts (e.g., limit to 3)."""
        return NewsArticle.objects.filter(featured=True).order_by('-created_at')[:limit]
    
    def __str__(self):
        return self.title
    

@receiver(post_delete, sender=NewsArticle)
def delete_cover_photo(sender, instance, **kwargs):
    if instance.photo and os.path.isfile(instance.photo.path):
        os.remove(instance.photo.path)

class RescueCategory(models.Model):
    # Define choices for the categories
    CAT = 'Cat'
    DOG = 'Dog'
    CATEGORY_CHOICES = [
        (CAT, 'Cat'),
        (DOG, 'Dog'),
    ]
    
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class AdoptableRescue(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(RescueCategory, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    picture = models.ImageField(upload_to='adoptable_rescues/', null=True, blank=True)
    additional_picture_1 = models.ImageField(upload_to='adoptable_rescues/additional/', null=True, blank=True)
    additional_picture_2 = models.ImageField(upload_to='adoptable_rescues/additional/', null=True, blank=True)
    additional_picture_3 = models.ImageField(upload_to='adoptable_rescues/additional/', null=True, blank=True)
    additional_picture_4 = models.ImageField(upload_to='adoptable_rescues/additional/', null=True, blank=True)


    def __str__(self):
        return self.name 
    
class GoogleForm(models.Model):
    title = models.CharField(max_length=100, default="Adoption Form")
    link = models.URLField(max_length=500, help_text="Enter the Google Forms URL")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title