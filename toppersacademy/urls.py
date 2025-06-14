"""
URL configuration for toppersacademy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

# Customize admin site
admin.site.site_header = "Toppers Academy Administration"
admin.site.site_title = "Toppers Academy Admin"
admin.site.index_title = "Welcome to Toppers Academy Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('results/', include('results.urls')),
    path('admissions/', include('admissions.urls')),
    path('gallery/', include('gallery.urls')),
    path('events/', include('events.urls')),
    path('about/branches/', include('about_branches.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

