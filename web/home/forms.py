from django.forms import EmailInput, ModelForm,TextInput,PasswordInput,NumberInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Offer

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude =['user','id','created_by']
        widgets ={
            'game' : TextInput(attrs={'placeholder': 'Game Name',  'style':'height:40px;' ,'size' : 60 , 'class':'form-control'}),
            'required_time' : TextInput(attrs={'placeholder': 'Required Time',  'style':'height:40px;' ,'size' : 60 , 'class':'form-control'}),
            'required_rank' : TextInput(attrs={'placeholder': 'Required Rank',  'style':'height:40px;' ,'size' : 60 , 'class':'form-control'}),
            'reward_ingame' : TextInput(attrs={'placeholder': 'Reward Ingame',  'style':'height:40px;' ,'size' : 60 , 'class':'form-control'}),
            'number_of_recruit_player' : NumberInput(attrs={'placeholder': 'Number of Recruit Player',  'style':'height:40px;' ,'size' : 60 , 'class':'form-control'}),
            'salary' : TextInput(attrs={'placeholder': 'Salary',  'style':'height:40px;' ,'size' : 60 , 'class':'form-control'}),
            'description' : TextInput(attrs={'placeholder': 'Description',  'style':'height:100px;' ,'size' : 60 , 'class':'form-control'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','password']
        widgets ={
                'username' : TextInput(attrs={'placeholder': 'Username', 'class':'form-control'}),
                'password' : PasswordInput(attrs={'placeholder': 'Password',  'class':'form-control'}),

        }

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        exclude =['id',]
        widgets ={
                'first_name' : TextInput(attrs={'placeholder': 'First name', 'class':'form-control'}),
                'last_name' : TextInput(attrs={'placeholder': 'Last name', 'class':'form-control'}),
                'username' : TextInput(attrs={'placeholder': 'Username', 'class':'form-control'}),
                'email' : EmailInput(attrs={'placeholder': 'Email', 'class':'form-control'}),
                'password' : PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}),
                'confirm_password' : PasswordInput(attrs={'placeholder': 'Confirm Password', 'class':'form-control'}),

        }
    
