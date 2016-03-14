from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField
from djangoratings.fields import RatingField
from django.db.models import Avg

# Create your models here.

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    parent_category = models.ForeignKey('self',blank=True,null=True)
    def __unicode__(self):
        return self.name


class Business(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    categories = models.ManyToManyField(Category)
    address = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=20,null=True)
    phone_number = models.CharField(max_length=12,null=True)
    web_address = models.URLField(null=True)
    photo = models.ImageField(null=True,upload_to='businesses/%Y/%m/%d')
    create_date = models.DateTimeField(auto_now_add=True,null=True)
    location = GeopositionField(null=True)
    approved = models.BooleanField(default=False)
    email = models.EmailField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    features = models.ManyToManyField('Features',null=True)
    description = models.TextField(null=True)
    price_range = models.IntegerField(null=True)

    def __unicode__(self):
        return self.name

    def get_no_reviews(self):
        return Review.objects.filter(business=self).count()
    def get_avg_rating(self):
        # get avg rating review for objects that were rated
        return Review.objects.filter(business=self,rating_score__range=(1,5)).aggregate(Avg('rating_score'))['rating_score__avg']




class Customer(models.Model):
    user = models.OneToOneField(User)
    photo = models.FileField(null=True,upload_to='avatars/%Y/%m/%d',blank=True)
    def __unicode__(self):
        return "%s %s" %(self.user.first_name,self.user.last_name)

class Review(models.Model):
    customer = models.ForeignKey(Customer,null=True)
    business = models.ForeignKey(Business,null=True)
    rating = RatingField(range=5,can_change_vote=True,allow_delete=True)
    review = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

class BusinessPhoto(models.Model):
    photo = models.ImageField(null=True,upload_to='businesses/%Y/%m/%d')
    review = models.ForeignKey(Review,null=True)

class Features(models.Model):
    name = models.CharField(max_length=255)
    def  __unicode__(self):
        return self.name

class EventCategory(models.Model):
    name = models.CharField(max_length=255)

class Event(models.Model):
    name = models.CharField(max_length=20,null=True)
    categories= models.ManyToManyField(EventCategory)
    event_date = models.DateTimeField(null=True)
    where = models.CharField(max_length=50,null=True)
    description = models.TextField(null=True)
    website_url = models.URLField(null=True)
    price = models.IntegerField(null=True)











