from django.urls import path
from . import views

app_name = 'about_branches'

urlpatterns = [
    path('dattanagar/', views.dattanagar, name='dattanagar'),
    path('ambegoan/', views.ambegoan, name='ambegoan'),
    path('narhe/', views.narhe, name='narhe'),
] 