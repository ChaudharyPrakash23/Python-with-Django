from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
        
def home(request):
    context={
        "name":"prakash chaudhary",
        "age":"23",
        "skills":['pyhton',"react","django"],
        "User":User('Sameer',26),
        "blog":{
            "title":"django templates intro",
            "author":{
                "name":"Rabindra nath tagore",
                "Quote":"some one is great"
            },
            "content":"<b>this is bold</b>",
            "created_at": datetime(2026,7,28,10,30)
        },
        "empty":None,
    }
    return render(request,"blog/home.html",context)