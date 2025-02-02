# Generated by Django 5.1.4 on 2025-01-28 02:17

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Adoption Form', max_length=100)),
                ('link', models.URLField(help_text='Enter the Google Forms URL', max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_section_bg_photo', models.ImageField(blank=True, null=True, upload_to='homepage/')),
                ('hero_section_title', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('hero_section_subtitle', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('hero_section_cta_btn_text', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('about_us_section_photo', models.ImageField(blank=True, null=True, upload_to='about_us/')),
                ('about_us_section_header', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('about_us_section_content', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomePageStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='homepage/')),
                ('number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RescueCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='wishlist/')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='news&articles/')),
                ('featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('summary', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_article', to='management.newsarticlecategory')),
            ],
        ),
        migrations.CreateModel(
            name='AdoptableRescue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='adoptable_rescues/')),
                ('additional_picture_1', models.ImageField(blank=True, null=True, upload_to='adoptable_rescues/additional/')),
                ('additional_picture_2', models.ImageField(blank=True, null=True, upload_to='adoptable_rescues/additional/')),
                ('additional_picture_3', models.ImageField(blank=True, null=True, upload_to='adoptable_rescues/additional/')),
                ('additional_picture_4', models.ImageField(blank=True, null=True, upload_to='adoptable_rescues/additional/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.rescuecategory')),
            ],
        ),
        migrations.CreateModel(
            name='EducationalResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='educational_resources/')),
                ('featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('summary', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='educational_resource', to='management.resourcecategory')),
            ],
        ),
    ]
