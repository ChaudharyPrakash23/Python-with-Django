from django.shortcuts import render
from datetime import datetime

def blog_list(request):
    context={
        
    }
return render(request,'blog/blog_list.html',context)    