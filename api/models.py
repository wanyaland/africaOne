from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Donor(models.Model):
    user = models.ForeignKey(User)
    fine= models.CharField(max_length=100)
    fine_price = models.IntegerField()
    total_fine = models.IntegerField()


