from django.db import models
from ckeditor.fields import RichTextField  
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

    
