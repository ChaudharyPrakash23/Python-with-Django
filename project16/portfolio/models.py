from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    city=models.CharField(max_length=20)
    
    def __str__(self):
        return (self.name)
    
class Profile(models.Model):
    bio=models.TextField()
    location=models.CharField(max_length=30)
    birth_date=models.DateField(null=True,blank=True)
    
    def __str__(self):
        return str(self.bio)