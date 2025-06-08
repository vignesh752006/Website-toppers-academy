from django.urls import path
from . import views

app_name = 'results'

urlpatterns = [
    path('', views.index, name='index'),
    path('10th-result/', views.result_10th, name='10th_result'),
    path('12th-result/', views.result_12th, name='12th_result'),
] 