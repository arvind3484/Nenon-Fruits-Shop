from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

def home(request):
    listdata=Destination.objects.all()
    return render(request,"index.html",{'listdata':listdata})

def about(request):
    return render(request,"about.html")
def fruit(request):
    return render(request,"fruit.html")
def contact(request):
    return render(request,"contact.html")
def testimonial(request):
    return render(request,"testimonial.html")



# Create your views here.
