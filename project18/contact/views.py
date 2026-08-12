from django.shortcuts import render,redirect
from django.http import HttpResponse
from contact.models import Contact

def contact_form(request):
    return render(request,'contact.html')

def submit_contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        message=request.POST.get('message')
        # created_at=request.POST.get('created_at')
        if name and message:
            Contact.objects.create(name=name,message=message)
            return HttpResponse (f"Thank you {name} for your message {message}")
        else:
            return HttpResponse("Please provide name and message")
        
    return redirect('contact_form')
        