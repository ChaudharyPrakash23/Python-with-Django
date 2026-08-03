from django.shortcuts import render

def home(request):
    return render(request,'base.html')

def blog(request):
    student_list=[
        {"name":"prakash","class":10},
        {"name":"akash","class":9},
        {"name":"kash","class":8},
    ]
    return render(request,'blog.html',{'students':student_list})
