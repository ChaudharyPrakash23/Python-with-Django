from django.shortcuts import render
from datetime import datetime

def blog_list(request):
    blogs=[
        {'title':'django basics','is_featured':True,"author":'john Doe','date':datetime(2023,10,1)},
        {'title':'React Baics','is_featured':False,"author":'Prakash chaudhary','date':datetime(2024,10,1)},
        {'title':'Express Basics','is_featured':False,"author":'','date':datetime(2025,10,1)}
    ]
    context={
        'blogs':blogs,
        "today":datetime.now(),
        "html_code":"<h1><b>welcome to my blog</b></h1>"
    }
    return render(request,'blog/blog_list.html',context)    