# Every view function takes at least one parameter: request (Atlast every thing comes here)
from django.shortcuts import render, HttpResponse
# To render a string we use HTTPResponse
# But we want to render HTML files, so we use render function.

# Create your views here.

from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    context = {
        "variable1": "This is sent from views.py",
        "variable2": "Myself Madhav Raizada"
    }
    return render(request, "index.html", context)

def index2(request):

    messages.success(request, "This is a success message")
    return render(request, "Bootstrap.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        # print(name, email, phone, desc)
        
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")  # Notification of successfull upload
    return render(request, "contact.html")