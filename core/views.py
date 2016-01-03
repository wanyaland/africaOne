from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from core.models import *
from django.views.generic import *
from django.core.urlresolvers import reverse
from djangoratings.views import AddRatingView,AddRatingFromModel
from django.contrib.contenttypes.models import ContentType


def index(request):
    return render(request,'core/index.html')

def logout_view(request):
    logout(request)
    return redirect('core:home')

def sign_up(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        customer_form = CustomerForm(request.POST,request.FILES)
        if  form.is_valid() and customer_form.is_valid() :
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

class ReviewListView(ListView):
    model = Business
    template_name = 'core/review_list.html'

class ReviewView(View):

    template_name='core/review_form.html'

    def get(self,request,*args,**kwargs):
        pk = self.kwargs.get('pk')
        business_pk = self.kwargs.get('business_pk')
        business = get_object_or_404(Business,pk=business_pk)
        if pk is None:
            review_form = ReviewForm()
        else:
            review = get_object_or_404(Review,pk=pk)
            review_form = ReviewForm(instance=review)
        return render(
            request,
            self.template_name,{
                'form':review_form,
                'action_url':reverse('core:review_edit',
                                     kwargs={'pk':pk}) if pk else reverse ('core:review_add',kwargs={'business_pk':business_pk}),
                'business':business
            }
        )

    def post(self,request,*args,**kwargs):
        pk = self.kwargs.get('pk')
        business_pk = self.kwargs.get('business_pk')
        if pk is not None:
            review = get_object_or_404(Review,pk=pk)
            review_form = ReviewForm(instance=review,data=request.POST)
        else:
            review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review=review_form.save(commit=False)
            business_pk=self.kwargs.get('business_pk')
            business = get_object_or_404(Business,pk=business_pk)
            review.business = business
            review.customer = Customer.objects.get(user=request.user)
            review.save()
            review_type = ContentType.objects.get_for_model(review)
            score = request.POST['rating']
            params = {
                'content_type_id':review_type.id,
                'object_id':review.id,
                'field_name': 'rating',
                'score':score,
            }
            response=AddRatingView()(request,**params)
            if response.status_code==200:
                return redirect('core:review_list')
            return {'error':9,'message':response.content}
        else:
            return render(
                request,self.template_name,{
                    'review_form':review_form,
                    'action_url':reverse('core:review_edit',kwargs={'pk':pk}) if pk else reverse('core:review_add',kwargs={'business_pk':business_pk})
                }
            )









