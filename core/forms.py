__author__ = 'wanyama'

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput,EmailInput
from models import Customer,Business,Review
from widgets import *
from django.forms.widgets import RadioFieldRenderer

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1':TextInput(attrs={'class':'form-control','placeholder': 'Password'}),
            'password2':TextInput(attrs={'class': 'form-control','placeholder': 'Repeat Password'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['photo']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields =('name','address','email','web_address','phone_number','city','categories','location','photo')
        widgets = {
            'name':TextInput(attrs={'class':'form-control','placeholder':'Business Name'}),
            'address':TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'email':EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'city':TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'phone_number':TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}),
            'web_address':TextInput(attrs={'class':'form-control','placeholder':'Web Address'}),
            'categories':forms.CheckboxSelectMultiple(),
        }

class ReviewForm(forms.ModelForm):
    RATING_CHOICES =((1,1),(2,2),(3,3),(4,4),(5,5),)
    rating=forms.CharField(widget=forms.RadioSelect(renderer=StarsRadioFieldRenderer,attrs={'class':'star'},choices=RATING_CHOICES))
    #rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class':'star'}))
    class Meta:
        model = Review
        fields = ('rating','review')

