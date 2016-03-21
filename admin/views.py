from django.shortcuts import render
from core.models import Business,Category
from django.views.generic import *

# Create your views here.

def index(request):
    return render(request,'admin/index.html')

class BusinessList(ListView):
    model = Business
    queryset = Business.objects.all()



