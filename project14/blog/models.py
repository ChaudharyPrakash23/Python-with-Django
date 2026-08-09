from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    enrollment_date=models.DateField(auto_now_add=True)
    city=models.CharField(max_length=30,default='unknown')
    
    def __str__(self):
        return self.name