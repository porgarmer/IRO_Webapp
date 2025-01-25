from management.models import (
    HomePage,
    NewsArticleCategory,
    NewsArticle)
from django import forms
from ckeditor.widgets import CKEditorWidget

class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = ['hero_section_bg_photo', 
                  'hero_section_title',
                  'hero_section_subtitle',
                  'hero_section_cta_btn_text']

class NewsArticleForm(forms.ModelForm):
    
    # content = forms.CharField(widget=CKEditorWidget(config_name='default'))  # Use full toolbar
    # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # photo = forms.CharField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = NewsArticle
        fields = ['title', 'content', 'category', 'photo']
