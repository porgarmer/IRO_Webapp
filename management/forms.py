from management.models import *
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from django_ckeditor_5.fields import CKEditor5Field
from django.forms import modelformset_factory

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
        


class AdoptableRescueForm(forms.ModelForm):
    class Meta:
        model = AdoptableRescue
        fields = ['name', 'category', 'description', 'picture', 'additional_picture_1', 'additional_picture_2', 'additional_picture_3', 'additional_picture_4']

    
AdoptableRescueFormSet = modelformset_factory(AdoptableRescue, form=AdoptableRescueForm, extra=1)

