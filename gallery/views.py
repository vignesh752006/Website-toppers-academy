from django.shortcuts import render

# Create your views here.

def gallery_index(request):
    return render(request, 'gallery/index.html')
