# Generated by Django 5.1.4 on 2025-01-22 09:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_homepage_hero_section_cta_btn_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about_us_section_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_us_section_header',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_us_section_photo',
            field=models.ImageField(blank=True, null=True, upload_to='about_us/'),
        ),
    ]