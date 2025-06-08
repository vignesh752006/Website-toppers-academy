from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'events/index.html')

def annual_function(request):
    return render(request, 'events/annualFunction.html')

def career_guidance(request):
    return render(request, 'events/career_guidance.html')

def sports_day(request):
    return render(request, 'events/sports_day.html')

def mock_test(request):
    return render(request, 'events/mock_test.html')
