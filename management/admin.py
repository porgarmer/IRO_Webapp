from django.contrib import admin
from management.models import (
    HomePage,
    NewsArticle,
    NewsArticleCategory,
)
# Register your models here.
admin.site.register(HomePage)
admin.site.register(NewsArticle)
admin.site.register(NewsArticleCategory)

    