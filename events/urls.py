from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('career-guidance/', views.career_guidance, name='career_guidance'),
    path('annual-function/', views.annual_function, name='annualFunction'),
    path('sports-day/', views.sports_day, name='sports_day'),
    path('mock-test/', views.mock_test, name='mock_test'),
] 