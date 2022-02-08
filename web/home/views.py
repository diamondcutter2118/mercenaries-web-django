from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import TextInput,ModelForm,NumberInput,EmailInput,PasswordInput
from .models import User , Offer
from django.contrib.auth import authenticate, login , logout
# Create your views here.
app_name = "home"

class LoginForm(forms.Form):
    username =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    password =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}))

class SignupForm(forms.Form):
    first_name =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name','class':'form-control'}))
    last_name =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name','class':'form-control'}))
    username =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    email =forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control'}))
    password =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}))
    confirm_password =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class':'form-control'}))

class RequirementForm(forms.Form):
    game = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Game Name',  'style':'height:40px;' ,'size' : 60 , 'class':'form-control'}))
    required_time = forms.CharField(widget =forms.TextInput(attrs ={'placeholder':'Required Time','size' : 60 ,'style':'height:40px;' ,'class':'form-control'}))
    required_rank = forms.CharField(widget =forms.TextInput(attrs ={'placeholder':'Required Rank','size' : 60 ,'style':'height:40px;' ,'class':'form-control'}))
    reward_ingame = forms.CharField(widget =forms.TextInput(attrs ={'placeholder':'Reward Ingame','size' : 60 ,'style':'height:40px;' ,'class':'form-control'}))
    number_of_recruit_player = forms.CharField(widget =forms.NumberInput(attrs ={'placeholder':'Number of Recruit Player','size' : 60 ,'style':'height:40px;' ,'class':'form-control'}))
    salary = forms.CharField(widget =forms.TextInput(attrs ={'placeholder':'Salary','size' : 60 ,'style':'height:40px;' ,'class':'form-control'}))
    description = forms.CharField(widget =forms.TextInput(attrs ={'placeholder':'Description', 'size' : 60 ,'style':'height:100px;' ,'class':'form-control'}))
    
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
    if request.method == "POST":

        form = RequirementForm(request.POST)

        if form.is_valid():
            # Should make a loop here
            game_form = form.cleaned_data["game"]
            required_time_form = form.cleaned_data["required_time"]
            required_rank_form = form.cleaned_data["required_rank"]
            reward_ingame_form = form.cleaned_data["reward_ingame"]
            salary_form = form.cleaned_data["salary"]
            description_form = form.cleaned_data["description"]
            
            request.session["game"] += [game_form]
            request.session["required_time"] += [required_time_form]
            request.session["required_rank"] += [required_rank_form]
            request.session["reward_ingame"] += [reward_ingame_form]
            request.session["salary"] += [salary_form]
            request.session["description"] += [description_form]

            game_model = request.POST["game"]
            required_time_model = request.POST["required_time"]
            required_rank_model = request.POST["required_rank"]
            reward_ingame_model = request.POST["reward_ingame"]
            salary_model = request.POST["salary"]
            description_model = request.POST["description"]

            # Should make a loop here
            requirement_data = Offer(game = game_model, required_time =required_time_model, required_rank = required_rank_model,reward_ingame =reward_ingame_model,salary=salary_model, description = description_model)
            requirement_data.save()

            return HttpResponseRedirect(reverse("home:posts"))
        else:

            return render(request, "home/posting.html", {
                "form": form
            })

    return render(request, "home/posting.html", {
        "form": RequirementForm()
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







