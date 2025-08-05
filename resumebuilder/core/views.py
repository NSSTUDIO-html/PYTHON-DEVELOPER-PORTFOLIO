# core/views.py
from django.shortcuts import render, redirect

from .forms import ResumeForm

def home(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()  # Now it works
            return redirect('home')  # Make sure 'home' is defined in your urls.py

    else:
        form = ResumeForm()
    return render(request, 'index.html', {'form': form})
