from django.contrib import admin
from management.models import *

# Register your models here.
admin.site.register(HomePage)
admin.site.register(NewsArticle)
admin.site.register(NewsArticleCategory)
admin.site.register(RescueCategory)
admin.site.register(AdoptableRescue)

    