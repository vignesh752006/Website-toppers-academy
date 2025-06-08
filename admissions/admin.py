from django.contrib import admin
from .models import Admission

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'parent_name', 'contact_number', 'standard', 'status', 'created_at')
    list_filter = ('status', 'standard', 'created_at')
    search_fields = ('student_name', 'parent_name', 'contact_number')
    ordering = ('-created_at',)
    list_editable = ('status',)
    list_per_page = 20
