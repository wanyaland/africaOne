from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from core.models import *
from django.views.generic import *
from django.core.urlresolvers import reverse

def index(request):
    return render(request,'core/index.html')

def logout_view(request):
    logout(request)
    return redirect('core:home')

def sign_up(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if  form.is_valid():
            user = form.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            user.save()
            customer.save()
            return redirect('core:home')
    else:
        form = RegistrationForm()
        customer_form = CustomerForm()
    return render(request,'core/sign_up.html',{
        'form':form,'customer_form':customer_form
    })


class BusinessListView(ListView):
    model = Business


class BusinesView(View):

    template_name = 'core/business_create.html'

    def get(self,request,*args,**kwargs):
        pk = self.kwargs.get('pk')
        if pk is None:
            business_form= BusinessForm()
        else:
            business = get_object_or_404(Business,pk=pk)
            business_form = BusinessForm(instance=business)
        return render(
            request,
            self.template_name,
            {
                'form':business_form,
                'action_url':reverse('core:business_edit',
                                     kwargs={'pk':pk} ) if pk else reverse('core:business_add')

            }
        )

    def post(self,request,*args,**kwargs):
        pk=self.kwargs.get('pk')
        if pk is not None:
            business = get_object_or_404(Business,pk=pk)
            business_form = BusinessForm(instance=business,data=request.POST)
        else:
            business_form = BusinessForm(request.POST)
        if business_form.is_valid():
            business_form.save()
            return redirect('core:add_business_successful')
        else:
            return render(
                request,self.template_name,
                {
                    'form':business_form,
                    'action_url':reverse('core:business_edit',kwargs={'pk':pk}) if pk else reverse('core:business_add')
                }
            )


def add_business_successful(request):
    return render(request,'core/business_successful.html')







