from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return rnder(request,'blog/about.html')