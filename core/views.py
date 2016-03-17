from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from core.models import *
from django.views.generic import *
from django.core.urlresolvers import reverse
from djangoratings.views import AddRatingView,AddRatingFromModel
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger




def index(request):
    review_list = Review.objects.all()
    categories = Category.objects.all()
    return render(request,'core/index.html',{
        'categories':categories,
    })

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
    def get_queryset(self):
        return Business.objects.filter(Business,name=self.args[0])


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
                'action_url':reverse('core:business_user_edit',kwargs={'pk':pk}) if pk else reverse('core:business_user_add'),
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
            return redirect('core:review_list')
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


class ReviewDetail(DetailView):
    model = Review

class BusinessDetail(DetailView):

    template_name = 'core/business_detail.html'
    model = Business

    def get_context_data(self, **kwargs):
        context = super(BusinessDetail,self).get_context_data(**kwargs)
        self.business =self.get_object()
        sort = self.request.GET.get('sort')
        if sort=='date':
         self.reviews = self.business.review_set.all().order_by('-create_date')
        elif sort=='rating':
         self.reviews = self.business.review_set.all().order_by('rating_score')
        else:
         self.reviews = self.business.review_set.all()
        self.categories = self.business.categories
        paginator = Paginator(self.reviews,5)
        page = self.request.GET.get('page')
        try:
            review_list = paginator.page(page)
        except PageNotAnInteger:
            review_list = paginator.page(1)
        except EmptyPage:
            review_list = paginator.page(paginator.num_pages)
        context['reviews'] = review_list
        business_set = []
        review_photos = []
        categories = self.categories.all()
        context['categories'] = categories
        for category in categories:
            for business in category.business_set.all():
                if business!= self.business:
                    business_set.append(business)
        context['business_set']= business_set[:3]
        for review in self.reviews:
            for photo in review.businessphoto_set.all():
                review_photos.append(photo)
        context['review_photos']=review_photos[:5]
        return context

class UserDetail(DetailView):
    template_name = 'core/user_detail.html'
    model=Customer

class UserList(ListView):
    template_name = 'core/user_list.html'
    model = Customer

class ClaimBusinessList(ListView):
    model=Business

def search_business(request):
    query = request.GET.get('business_name','')
    location = request.GET.get('location','')
    if query :
        qset = (
            Q(name__icontains=query)
        )
        results = Business.objects.filter(qset).distinct()
    else:
        results = []
    return render(request,'core/business_list.html',{
        'results':results,
        'query':query,
    })

class BusinessList(ListView):
    model = Business
    paginate_by = 30


class ReviewCreate(CreateView):
    form_class = ReviewForm
    template_name = 'core/review_form.html'

    def get_success_url(self):
        return reverse('core:review_list')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('business_pk')
        business = get_object_or_404(Business,pk=pk)
        review_list = Review.objects.filter(business=business)
        context = super(CreateView,self).get_context_data(**kwargs)
        context['business']=business
        context['reviews']=review_list
        return context

    def form_valid(self,form):

        context = self.get_context_data()
        form.instance.business = context['business']
        #form.instance.rating.add(score=self.request.POST['rating'],user=self.request.user,ip_address=self.request.META['REMOTE_ADDR'])
        image_list =    self.request.FILES.getlist('files')
        response=super(ReviewCreate,self).form_valid(form)
        review_type = ContentType.objects.get_for_model(self.object)
        score = self.request.POST['rating']
        params = {
                'content_type_id':review_type.id,
                'object_id':self.object.id,
                'field_name': 'rating',
                'score':score,
         }
        AddRatingView()(self.request,**params)
        for file in image_list:
            BusinessPhoto.objects.create(photo=file,review=self.object)
        return response


class ReviewEdit(UpdateView):
    form_class=ReviewForm
    template_name = 'core/review_form.html'

class ReviewDelete(DeleteView):
    model = Review

