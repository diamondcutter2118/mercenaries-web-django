from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def decentraland (request):
    return render (request, "games/Decentraland.html" )

def axieinfinity (request):
    return render (request, "games/Axieinfinity.html" )

def alienworld (request):
    return render (request, "games/Alienworld.html" )