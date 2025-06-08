from django.shortcuts import render

# Create your views here.

def dattanagar(request):
    return render(request, 'about_branches/dattanagar.html')

def ambegoan(request):
    return render(request, 'about_branches/ambegoan.html')

def narhe(request):
    return render(request, 'about_branches/narhe.html')
