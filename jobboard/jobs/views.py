# jobs/views.py

from django.shortcuts import render, get_object_or_404
from .models import Job

def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, 'jobs/job_detail.html', {'job': job})

