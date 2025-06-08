from django.db import models

# Create your models here.
class MediaItem(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )
    title = models.CharField(max_length=100)
    media_type = models.CharField(choices=MEDIA_TYPES, max_length=10)
    file = models.FileField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title