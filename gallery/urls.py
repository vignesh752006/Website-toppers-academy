from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.index, name='index'),
] 

from .views import gallery_view

urlpatterns = [
    path('', gallery_view, name='index'),
]