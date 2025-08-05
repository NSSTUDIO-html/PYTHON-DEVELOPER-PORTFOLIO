from django.shortcuts import render
from .models import Student, Teacher

def home(request):
    return render(request, 'core/home.html')

def students(request):
    students = Student.objects.all()
    return render(request, 'core/students.html', {'students': students})

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'core/teachers.html', {'teachers': teachers})
