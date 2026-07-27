from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("<h1>welcome to home page</h1>cd ")

def about(request):
    a=10
    b=30
    return HttpResponse(f"About page returns {a+b}");
    