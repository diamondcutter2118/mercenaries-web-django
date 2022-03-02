from django.forms import EmailInput, ModelForm,TextInput,PasswordInput,NumberInput,FileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Offer,Customer

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude =['user','id','created_by']
        widgets ={
            'game' : TextInput(attrs={'placeholder': 'Game Name', 'class':'form-control'}),
            'required_time' : TextInput(attrs={'placeholder': 'Required Time',  'class':'form-control'}),
            'required_rank' : TextInput(attrs={'placeholder': 'Required Rank',  'class':'form-control'}),
            'reward_ingame' : TextInput(attrs={'placeholder': 'Reward Ingame', 'class':'form-control'}),
            'number_of_recruit_player' : NumberInput(attrs={'placeholder': 'Number of Recruit Player' , 'class':'form-control'}),
            'salary' : TextInput(attrs={'placeholder': 'Salary', 'class':'form-control'}),
            'description' : TextInput(attrs={'placeholder': 'Description' , 'class':'form-control'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields =['username','password']
        widgets ={
                'username' : TextInput(attrs={'placeholder': 'Username', 'class':'form-control'}),
                'password' : PasswordInput(attrs={'placeholder': 'Password',  'class':'form-control'}),

        }

class CreateUserForm(ModelForm):
    class Meta:
        model = Customer
        fields =['username','email','password','confirm_password']
        widgets ={
                'username' : TextInput(attrs={'placeholder': 'Username', 'class':'form-control'}),
                'email' : EmailInput(attrs={'placeholder': 'Email', 'class':'form-control'}),
                'password' : PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}),
                'confirm_password' : PasswordInput(attrs={'placeholder': 'Confirm Password', 'class':'form-control'}),

        }
    
class CustomerForm (ModelForm):
    class Meta:
        model = Customer
        exclude=['user','id','confirm_password','date_created']
        widget ={
                'username' : TextInput(attrs={'placeholder': 'Username', 'class':'form-control'}),
                'email' : EmailInput(attrs={'placeholder': 'Email', 'class':'form-control'}),
                'password' : PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}),
                'profile_pic' : FileInput(attrs={'placeholder': 'Image', 'class':'form-control'}),
        }