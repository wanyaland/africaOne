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
    review_list = Review.objects.all()
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


class BusinessListView(View):
    model = Business
    template_name = 'core/business_list.html'
    def get(self, request, *args, **kwargs):
        search_form = BusinessSearchForm()
        business_list = Business.objects.all()
        return render(request,self.template_name,
                      {'search_form':search_form,'business_list':business_list,})

    def post(self,request,*args,**kwargs):
        name=''
        search_form = BusinessSearchForm(request.POST)
        if search_form.is_valid():
            name=search_form.cleaned_data['name']
        business_list = Business.objects.filter(name=name)
        return render(request,
                      self.template_name,{
                          'search_form':search_form,
                          'business_list':business_list,
                      })


class BusinessUserView(View):
    template_name = 'core/business_user.html'

    def get(self,request,*args,**kwargs):
        customer = Customer.objects.filter(user=request.user)
        pk = self.kwargs.get('pk')
        if pk is None:
            business_form = BusinessForm()
            review_form = ReviewForm()
        else:
            review = get_object_or_404(Review,pk=pk)
            business = Review.objects.filter(review=review,customer=customer)
            review_form = ReviewForm(instance=review)
            business_form = BusinessForm(instance=business)
        return render(
            request,
            self.template_name,{
               'review_form':review_form,
                'business_form':business_form,
                'action_url':reverse('core:business_user_edit',kwargs={'pk':pk}) if pk else reverse('core:business_user_add')
            }
        )

    def post(self,request,*args,**kwargs):
        customer = Customer.objects.filter(user=request.user)
        pk = self.kwargs.get('pk')
        if pk is None:
            review_form = ReviewForm(request.POST)
            business_form = BusinessForm(request.POST,request.FILES)
        else:
            review = get_object_or_404(Review,pk=pk)
            business = Review.objects.filter(review=review,customer=customer)
            review_form = ReviewForm(instance=review,data=request.POST)
            business_form = BusinessForm(instance=business,data=request.POST,files=request.FILES)
        if business_form.is_valid() and review_form.is_valid():
            review = review_form.save(commit=False)
            business = business_form.save()
            review.business= business
            review.customer = Customer.objects.get(user=request.user)
            review.save()
            review_type = ContentType.objects.get_for_model(review)
            score = review.POST['rating']
            params = {
                'content_type_id':review_type.id,
                'object_id':review.id,
                'field_name': 'rating',
                'score':score,
            }
            AddRatingView()(request,**params)
            return redirect('core:business_user_list')
        else:
            return render(request,
                      self.template_name,{
                        'review_form':review_form,
                        'business_form':business_form,
                        'action_url':reverse('core:business_user_edit',kwargs={'pk':pk}) if pk else reverse('core:business_user_add'),
                      })



class BusinesView(View):

    template_name = 'core/business_create.html'

    def get(self,request,*args,**kwargs):
        pk = self.kwargs.get('pk')
        if pk is None:
            business_form= BusinessForm()
        else:
            business = get_object_or_404(Business,pk=pk)
            business_form = BusinessForm(instance=business,files=request.FILES)
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
            business_form = BusinessForm(instance=business,data=request.POST,files=request.FILES)
        else:
            business_form = BusinessForm(request.POST,request.FILES)
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
        review_list = Review.objects.filter(business=business)
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
                'business':business,
                'reviews':review_list,
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
            AddRatingView()(request,**params)
            return redirect('core:review_list')
        else:
            return render(
                request,self.template_name,{
                    'review_form':review_form,
                    'action_url':reverse('core:review_edit',kwargs={'pk':pk}) if pk else reverse('core:review_add',kwargs={'business_pk':business_pk})
                }
            )


class ReviewDetail(DetailView):
    model = Review






