from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField
from djangoratings.fields import RatingField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Business(models.Model):
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
    rating = RatingField(range=5)

    def __unicode__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User)
    photo = models.FileField(null=True,upload_to='avatars/%Y/%m/%d',blank=True)
    def __unicode__(self):
        return "%s %s" %(self.user.first_name,self.user.last_name)

class Event(models.Model):
    event_name = models.CharField(max_length=20)
    event_date = models.DateTimeField()
    def __unicode__(self):
        return self.event_name




