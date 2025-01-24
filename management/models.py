from django.db import models
from ckeditor.fields import RichTextField  
from datetime import datetime

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

class NewsArticle(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='news&articles/')
    # author =  # to be added
    date_published = models.DateField(auto_now_add=False, auto_now=False, default=datetime.today, null=True)
    category = models.ForeignKey(NewsArticleCategory, null=True, blank=True, related_name='news_article', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
