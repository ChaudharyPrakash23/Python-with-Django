from django.shortcuts import render
from .models import Student

def Student_list(request):
    students=Student.objects.all()
    return render(request,'portfolio/student_list.html',{'students':students})