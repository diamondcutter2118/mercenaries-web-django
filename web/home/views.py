from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import TextInput,ModelForm,NumberInput,EmailInput,PasswordInput, inlineformset_factory
from pkg_resources import Requirement
from .models import User , Offer, Game
from django.contrib.auth import authenticate, login , logout
from .forms import OfferForm,LoginForm,SignupForm
from django.forms import inlineformset_factory
# Create your views here.
app_name = "home"
    
def login_view (request):
    if request.method == "POST":
        
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("home:loged_in_index"))
        
        else:
            return render(request, "home/login.html", {
                "message": "Invalid Credentials"
            })

    return render (request, "home/login.html",{
        "login_form" :LoginForm()
    })

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]

        signup_data = User(first_name = first_name,last_name = last_name, email = email, password =password)
        signup_data.save()

    return render (request, "home/signup.html",{
         "signup_form" : SignupForm()
    })

def logout_view(request):
    logout(request)
    return render(request, "home/login.html", {
                "message": "Logged Out"
            })

def posts(request):

    if "game" and "required_time"  and "required_rank" and "reward_ingame" and "salary" and "description" not in request.session :

        request.session["game"] = []
        request.session["required_time"] = []
        request.session["required_rank"] = []
        request.session["reward_ingame"] = []
        request.session["salary"] = []
        request.session["description"] = []

    return render(request, "home/posts.html", {
        "game": request.session["game"],
        "required_time": request.session["required_time"],
        "required_rank": request.session["required_rank"],
        "reward_ingame": request.session["reward_ingame"],
        "salary": request.session["salary"],
        "description": request.session["description"],
    }) 

def posting(request):  
    form = OfferForm()
    if request.method =="POST":
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()

    return render (request, "home/posting.html",{
        "form":form
    })
    
def newsfeed (request):
    return render (request, "home/newsfeed.html")

def games (request):
    return render (request, "home/games.html")

def chat (request):
    return render (request, "home/chat.html")

def index(request):
     return render (request, "home/index.html")

def loged_in_index(request):
     return render (request, "home/loged_in_index.html")






