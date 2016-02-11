__author__ = 'wanyama'

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput,EmailInput
from models import Customer,Business,Review,BusinessPhoto,Event
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
    rating = forms.CharField(widget=forms.NumberInput(attrs={'class':'rating','data-min':'1','data-max':'5','step':'0.5','type':'number','id':'input-id','data-size':'xs',}))
    class Meta:
        model = Review
        fields = ('rating','review',)

class BusinessSearchForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Near:'}))

class PhotoForm(forms.ModelForm):
    class Meta:
        model=BusinessPhoto
        fields=('photo',)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields=('name',)





