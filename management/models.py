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

class HomePageStats(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(null=True, blank=True, upload_to='homepage/')
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.pk:
            old_file = HomePageStats.objects.get(pk=self.pk).logo
            if old_file and old_file != self.logo and os.path.isfile(old_file.path):
                os.remove(old_file.path)    
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

@receiver(post_delete, sender=HomePageStats)
def delete_logo(sender, instance, **kwargs):
    if instance.logo and os.path.isfile(instance.logo.path):
        os.remove(instance.logo.path)
        

class Wishlist(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='wishlist/')
    name = models.CharField(max_length=50, unique=True)
    description = CKEditor5Field(blank=True, null=True, config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def save(self, *args, **kwargs):
        if self.pk:
            old_file = Wishlist.objects.get(pk=self.pk).photo
            if old_file and old_file != self.photo and os.path.isfile(old_file.path):
                os.remove(old_file.path)    
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
@receiver(post_delete, sender=Wishlist)
def delete_logo(sender, instance, **kwargs):
    if instance.photo and os.path.isfile(instance.photo.path):
        os.remove(instance.photo.path)

        
class NewsArticleCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class NewsArticle(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='news&articles/')
    featured = models.BooleanField(default=False)  # New field for featured posts
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(NewsArticleCategory, null=True, blank=True, related_name='news_article', on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    summary = CKEditor5Field(blank=True, null=True, config_name='extends')
    content = CKEditor5Field(blank=True, null=True, config_name='extends')
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)  # Create slug from title
            slug = base_slug
            counter = 1
            while NewsArticle.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"  # Append a counter for uniqueness
                counter += 1
            self.slug = slug
            
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


class ResourceCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class EducationalResource(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='educational_resources/')
    featured = models.BooleanField(default=False)  # New field for featured posts

    # author =  # to be added
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(ResourceCategory, null=True, blank=True, related_name='educational_resource', on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    summary = CKEditor5Field(blank=True, null=True, config_name='extends')
    content = CKEditor5Field(blank=True, null=True, config_name='extends')
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)  # Create slug from title
            slug = base_slug
            counter = 1
            while EducationalResource.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"  # Append a counter for uniqueness
                counter += 1
            self.slug = slug
            
        if self.pk:
            old_file = EducationalResource.objects.get(pk=self.pk).photo
            if old_file and old_file != self.photo and os.path.isfile(old_file.path):
                os.remove(old_file.path)    
        super().save(*args, **kwargs)
        
        
    @staticmethod
    def get_featured_posts(limit=1):
        """Get the latest featured posts (e.g., limit to 3)."""
        return EducationalResource.objects.filter(featured=True).order_by('-created_at')[:limit]
    
    def __str__(self):
        return self.title
    

@receiver(post_delete, sender=EducationalResource)
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
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(RescueCategory, on_delete=models.SET_NULL, null=True, blank=True)
    description = CKEditor5Field(blank=True, null=True, config_name='extends')
    profile = models.ImageField(upload_to='adoptable_rescues/', null=True, blank=True)
    additional_picture_1 = models.ImageField(upload_to='adoptable_rescues/additional/', null=True, blank=True)
    additional_picture_2 = models.ImageField(upload_to='adoptable_rescues/additional/', null=True, blank=True)
    additional_picture_3 = models.ImageField(upload_to='adoptable_rescues/additional/', null=True, blank=True)
    additional_picture_4 = models.ImageField(upload_to='adoptable_rescues/additional/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        
        if self.pk:
            rescue= AdoptableRescue.objects.get(pk=self.pk)
            old_profile = rescue.profile
            old_additional_picture_1 = rescue.additional_picture_1
            old_additional_picture_2 = rescue.additional_picture_2
            old_additional_picture_3 = rescue.additional_picture_3
            old_additional_picture_4 = rescue.additional_picture_4

            if old_profile and old_profile != self.profile and os.path.isfile(old_profile.path):
                os.remove(old_profile.path)    
                
            if old_additional_picture_1 and old_additional_picture_1 != self.additional_picture_1 and os.path.isfile(old_additional_picture_1.path):
                os.remove( old_additional_picture_1 .path)    
            
            if old_additional_picture_2 and old_additional_picture_2 != self.additional_picture_2 and os.path.isfile(old_additional_picture_2.path):
                os.remove(old_additional_picture_2.path)    
                
            if old_additional_picture_3 and old_additional_picture_3 != self.additional_picture_3 and os.path.isfile(old_additional_picture_3.path):
                os.remove(old_additional_picture_3.path)    
                
            if old_additional_picture_4 and old_additional_picture_4 != self.additional_picture_4 and os.path.isfile(old_additional_picture_4.path):
                os.remove(old_additional_picture_4.path)    
                
        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.name 
    
@receiver(post_delete, sender=AdoptableRescue)
def delete_cover_photo(sender, instance, **kwargs):
    if instance.profile and os.path.isfile(instance.profile.path):
        os.remove(instance.profile.path)
    if instance.additional_picture_1 and os.path.isfile(instance.additional_picture_1.path):
        os.remove(instance.additional_picture_1.path)
    if instance.additional_picture_2 and os.path.isfile(instance.additional_picture_2.path):
        os.remove(instance.additional_picture_2.path)
    if instance.additional_picture_3 and os.path.isfile(instance.additional_picture_3.path):
        os.remove(instance.additional_picture_3.path)
    if instance.additional_picture_4 and os.path.isfile(instance.additional_picture_4.path):
        os.remove(instance.additional_picture_4.path)


    
class GoogleForm(models.Model):
    title = models.CharField(max_length=100, default="Adoption Form")
    link = models.URLField(max_length=500, help_text="Enter the Google Forms URL")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
class Faq(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = CKEditor5Field(blank=True, null=True, config_name='extends')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title