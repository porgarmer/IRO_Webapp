from management.models import (
    HomePage,
    NewsArticleCategory,
    NewsArticle)
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from django_ckeditor_5.fields import CKEditor5Field

class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = ['hero_section_bg_photo', 
                  'hero_section_title',
                  'hero_section_subtitle',
                  'hero_section_cta_btn_text']

class NewsArticleForm(forms.ModelForm):
    
    class Meta:
        model = NewsArticle
        fields = ['title', 'content', 'category', 'photo']
        widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control shadow-sm', 'placeholder': 'Enter title'}),
                    "content": CKEditor5Widget(
                        attrs={"class": "django_ckeditor_5"}, config_name="extends"
                    ),
                    'category': forms.Select(attrs={'class': 'form-control shadow-sm'}),
                    'photo': forms.ClearableFileInput(attrs={'class': 'form-control shadow-sm'}),
                }
        
