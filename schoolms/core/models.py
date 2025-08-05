from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10, unique=True)

    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.roll_no})"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
