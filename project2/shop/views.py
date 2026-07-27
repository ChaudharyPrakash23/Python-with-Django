from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("shop home page")

def products(response):
    return HttpResponse("product listings are done here")
# Create your views here.
