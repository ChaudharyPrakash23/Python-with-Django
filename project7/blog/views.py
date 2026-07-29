from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    post={
        'title':'seond template lecture',
        'description':'django is high level python framework',
        'author':None,
        'created_at':datetime.now(),
        'comment_count':5,
        'tags':['Django',"python",'webdev'],
        'price':100,
        "number":7
    }
    return render(request,'blog/blog_details.html',{"post":post})