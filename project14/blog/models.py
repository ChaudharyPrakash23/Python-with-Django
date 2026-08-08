from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(max_length=3)
    email=models.EmailField(unique=True)
    enrollment_date=models.DateField(auto_now_add=True)