from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# to be converted to a loop function #

def offer1 (request):
    return render (request, "offers/offer1.html")

def offer2 (request):
    return render (request, "offers/offer2.html")

def offer3 (request):
    return render (request, "offers/offer3.html")