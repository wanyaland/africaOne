from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=20)
    categories = models.ManyToManyField(Category)
    def __unicode__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User)
    def __unicode__(self):
        return "%s %s" %(self.user.first_name,self.user.last_name)

class Event(models.Model):
    event_name = models.CharField(max_length=20)
    event_date = models.DateTimeField()
    def __unicode__(self):
        return self.event_name




