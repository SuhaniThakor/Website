from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages



# Create your views here.
def index(request):
    context={
        "variable": "this is sent"
    }
   

    return render(request, 'index.html', context)
    #return HttpResponse("This is home page")
    
def about(request):
     return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
     return render(request, 'services.html')
    #return HttpResponse("This is services page")
    
def digital(request):
        return render(request, 'digital.html')

def contact(request):
    if request.method == "post":
        name = request.post.get('name')
        designation = request.post.get('designation')
        email = request.post.get('email')
        phone = request.post.get('phone')
        desc = request.post.get('desc')
        contact = Contact(name=name, designation=designation, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


    #return HttpResponse("This is contact page")