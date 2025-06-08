from django.shortcuts import render

# Create your views here.
from .models import MediaItem
def index(request):
    return render(request, 'gallery/index.html')

def gallery_view(request):
    media_items = MediaItem.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/index.html', {'media_items': media_items})