from django.db import models

# Create your models here.

class Admission(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('responded', 'Responded'),
    ]
    
    parent_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    standard = models.CharField(max_length=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.standard}th Standard"

    class Meta:
        verbose_name = "Admission"
        verbose_name_plural = "Admissions"
