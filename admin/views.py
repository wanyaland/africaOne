from django.shortcuts import render
from core.models import Business,Category
from django.views.generic import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.


class BusinessList(ListView):
    model = Business
    queryset = Business.objects.all()
    template_name = 'admin/index.html'
    paginate_by = 50
    




