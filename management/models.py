from django.db import models
from ckeditor.fields import RichTextField  
from datetime import datetime
from django.utils.text import slugify


# Create your models here.
class HomePage(models.Model):
    #hero section fields
    hero_section_bg_photo = models.ImageField(null=True, blank=True, upload_to='homepage/')
    hero_section_title = RichTextField(blank=True, null=True)
    hero_section_subtitle = RichTextField(blank=True, null=True)
    hero_section_cta_btn_text = RichTextField(blank=True, null=True)
    
    #about us section fields
    about_us_section_photo = models.ImageField(null=True, blank=True, upload_to='about_us/')
    about_us_section_header = RichTextField(blank=True, null=True)
    about_us_section_content = RichTextField(blank=True, null=True)

class NewsArticleCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class NewsArticle(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='news&articles/')
    # author =  # to be added
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(NewsArticleCategory, null=True, blank=True, related_name='news_article', on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
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