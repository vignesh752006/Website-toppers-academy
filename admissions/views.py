from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdmissionForm

# Create your views here.

def index(request):
    form = AdmissionForm()
    return render(request, 'admissions/index.html', {'form': form})

def admission_form(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Admission form submitted successfully!')
            return redirect('admissions:success')
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'admissions/index.html', {'form': form})
    return redirect('admissions:admissions_index')

def success(request):
    return render(request, 'admissions/success.html')
