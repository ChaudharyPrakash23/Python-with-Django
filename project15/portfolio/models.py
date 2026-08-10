from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    city=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name