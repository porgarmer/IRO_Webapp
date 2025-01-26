"""
URL configuration for IRO_Webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('shelters/', include('shelters_page.urls')),
    path('donate/', include('donate_page.urls')),
    path('iro-faqs/', include('faqs_page.urls')),
    path('adoption/', include('adoption.urls')),
    path('adoption-process/', include('adoption_process.urls')),
    path('management/', include('management.urls')),
    path('educational-resources/', include('educ_reso.urls')),
    path('news&articles/', include('news_artic.urls')),
    path('volunteer/', include('volunteer.urls')),
    path('content-page/', include('content_page.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
