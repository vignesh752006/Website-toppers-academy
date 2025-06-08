from django.urls import path
from . import views

app_name = 'admissions'

urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', views.admission_form, name='admission_form'),
    path('success/', views.success, name='success'),
] 