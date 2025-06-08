from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'results/index.html')

def result_10th(request):
    return render(request, 'results/10result.html')

def result_12th(request):
    return render(request, 'results/12result.html')
