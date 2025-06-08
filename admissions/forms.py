from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['parent_name', 'student_name', 'contact_number', 'standard']
        
    def clean_parent_name(self):
        parent_name = self.cleaned_data.get('parent_name')
        if len(parent_name) < 5:
            raise forms.ValidationError("Parent's name must be at least 5 letters long")
        return parent_name
        
    def clean_student_name(self):
        student_name = self.cleaned_data.get('student_name')
        if len(student_name) < 5:
            raise forms.ValidationError("Student's name must be at least 5 letters long")
        return student_name
        
    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if not contact_number.isdigit() or len(contact_number) != 10:
            raise forms.ValidationError("Please enter a valid 10-digit phone number")
        return contact_number 