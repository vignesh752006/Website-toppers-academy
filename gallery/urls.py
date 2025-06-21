from django.urls import path
from .views import gallery_index

app_name = 'gallery'

urlpatterns = [
    path('', gallery_index, name='index'),
] 