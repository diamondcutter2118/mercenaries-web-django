from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import TextInput,ModelForm,NumberInput,EmailInput,PasswordInput, inlineformset_factory
from django.contrib.auth.decorators import login_required
from .models import User , Offer, Game,Customer
from django.contrib.auth import authenticate, login , logout
from .forms import OfferForm,LoginForm,CreateUserForm,CustomerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group
# Create your views here.

app_name = "home"

@unauthenticated_user
def signup_view(request):
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username =form.cleaned_data.get('username')
                
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                User.objects.create(
                    user = user,
                )
                
                messages.success(request,"Account was created for " + user)
                
                return redirect('home: login')

        return render (request, "home/signup.html",{
            "form" : CreateUserForm()
        }) 

@unauthenticated_user
def login_view (request):
        if request.method == "POST":
            
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None :
                login(request, user)
                return HttpResponseRedirect(reverse("home:landing"))
            
            else:
                return render(request, "home/login.html", {
                    "message": "Invalid Credentials"
                })

        return render (request, "home/login.html",{
            "login_form" :LoginForm()
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

@login_required(login_url= "home:login")
@allowed_users(allowed_roles=['customer'])
def posting(request):  
    form = OfferForm()
    if request.method =="POST":
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()

    return render (request, "home/posting.html",{
        "form":form
    })

@allowed_users(allowed_roles=['customer'])
def userpage(request):
    customer = request.user.customer
    form = CustomerForm(instance =customer)
    context ={'form':form}
    return render (request, "home/userpage.html",context)

def newsfeed (request):
    return render (request, "home/newsfeed.html",{
        
    })

def games (request):
    return render (request, "home/games.html")

@login_required(login_url= "home:login")
@allowed_users(allowed_roles=['customer'])
def chat (request):
    return render (request, "home/chat.html")

def index(request):
     return render (request, "home/index.html")

@login_required(login_url= "home:login")
@allowed_users(allowed_roles=['customer'])
def landing(request):
     return render (request, "home/landing.html")






