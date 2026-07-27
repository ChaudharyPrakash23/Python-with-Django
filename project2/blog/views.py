from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Blog home page")

def about(response):
    return HttpResponse("About page")
# Create your views here.
