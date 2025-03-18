from management.models import *
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from django_ckeditor_5.fields import CKEditor5Field
from django.forms import modelformset_factory
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class EditUserForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control shadow-sm', 'type': 'password'}))
    new_password1 = forms.CharField(label='New Password', max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control shadow-sm', 'type': 'password'}))
    new_password2 = forms.CharField(label='Confirm New Password', max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control shadow-sm', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class HomePageHeroSectionForm(forms.ModelForm):
    hero_section_bg_photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))

    class Meta:
        model = HomePageHero
        fields = ['hero_section_bg_photo',
                  'hero_section_heading',
                  'hero_section_subheading',
                  ]
        widgets = {
            'hero_section_heading': CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="extends"),
            'hero_section_subheading': forms.TextInput(attrs={"class": "form-control shadow-sm", "placeholder": "Enter subheading"}),
        }
        
class HomePageAboutUsSectionForm(forms.ModelForm):
    about_us_section_photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))

    class Meta:
        model = HomePageAboutUs
        fields = ['about_us_section_photo',
                  'about_us_section_content',
                  ]
        widgets = {
            'about_us_section_content': CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="extends"),
        }

class HomePageVMGOForm(forms.ModelForm):
    bg_photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    
    class Meta:
        model = HomePageVMGO
        fields = ['bg_photo', 'vision', 'mission', 'goal']
        widgets = {
            'vision': forms.Textarea(attrs={'class': 'form-control shadow-sm'}),
            'mission': forms.Textarea(attrs={'class': 'form-control shadow-sm'}),
            'goal': forms.Textarea(attrs={'class': 'form-control shadow-sm'}),
        }

class HomePageStatsForm(forms.ModelForm):
    logo = forms.ImageField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    
    class Meta:
        model = HomePageStats
        fields = ['name', 'logo', 'number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control shadow-sm', 'placeholder': 'Enter category name'}),
            'number': forms.NumberInput(attrs={'class': 'form-control shadow-sm',
                                               'placeholder': 'Enter stat number',
                                               })
        }


class WishlistForm(forms.ModelForm):
    photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))

    class Meta:
        model = Wishlist
        fields = ['name', 'description', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control shaow sm', 'placeholder': 'Enter wishlist name'}),
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
        }


class ResourceCategoryForm(forms.ModelForm):
    class Meta:
        model = ResourceCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control shadow-sm', 'placeholder': 'Enter category name'})
        }


class EducationalResourceForm(forms.ModelForm):
    photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    category = forms.ModelChoiceField(queryset=ResourceCategory.objects.all().order_by(
        'name'), widget=forms.Select(attrs={'class': 'form-control shadow-sm'}))

    class Meta:
        model = EducationalResource
        fields = ['title', 'content', 'featured', 'category', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control shadow-sm', 'placeholder': 'Enter title'}),
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
            "summary": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class NewsArticleCategoryForm(forms.ModelForm):
    class Meta:
        model = NewsArticleCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control shaow sm', 'placeholder': 'Enter category name'})
        }


class NewsArticleForm(forms.ModelForm):
    photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    category = forms.ModelChoiceField(queryset=NewsArticleCategory.objects.all().order_by(
        'name'), widget=forms.Select(attrs={'class': 'form-control shadow-sm'}))

    class Meta:
        model = NewsArticle
        fields = ['title', 'content', 'featured', 'category', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control shadow-sm', 'placeholder': 'Enter title'}),
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
            "summary": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AdoptableRescueForm(forms.ModelForm):
    profile = forms.ImageField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    additional_picture_1 = forms.ImageField(label='Picture 1', required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    additional_picture_2 = forms.ImageField(label='Picture 2', required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    additional_picture_3 = forms.ImageField(label='Picture 3', required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    additional_picture_4 = forms.ImageField(label='Picture 4', required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))

    class Meta:
        model = AdoptableRescue
        fields = ['name', 'category', 'description', 'profile', 'additional_picture_1',
                  'additional_picture_2', 'additional_picture_3', 'additional_picture_4']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control shadow-sm', 'placeholder': 'Enter name'}),
            'category': forms.Select(attrs={'class': 'form-control shadow-sm'}),
            'description': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
        }


AdoptableRescueFormSet = modelformset_factory(
    AdoptableRescue, form=AdoptableRescueForm, extra=1)

class ShelterForm(forms.ModelForm):
    photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    picture_1 = forms.ImageField(label='Picture 1', required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    picture_2 = forms.ImageField(label='Picture 2', required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    picture_3 = forms.ImageField(label='Picture 3', required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    picture_4 = forms.ImageField(label='Picture 4', required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control shadow-sm', 'accept': 'image/*'}))
    
    class Meta:
        model = Shelter
        fields = ['photo', 'name', 'visitation', 'location', 'description', 
                  'picture_1', 'picture_2', 'picture_3', 'picture_4']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control shadow-sm', 'placeholder': 'Enter name'}),
            'location': forms.TextInput(attrs={'class': 'form-control shadow-sm', 'placeholder': 'Enter name'}),
            'visitation': forms.TextInput(attrs={'class': 'form-control shadow-sm', 'placeholder': 'Enter name'}),
            'description': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
        }
        
        labels = {
            'visitation': 'Visitors allowed'
        }

class GoogleFormForm(forms.ModelForm):
    class Meta:
        model = GoogleForm
        fields = ['title', 'link']


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control shadow-sm', 'placeholder': 'Enter name'}),
            'description': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
        }
