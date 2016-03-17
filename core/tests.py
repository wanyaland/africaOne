from django.test import TestCase
from models import Business,Review,Customer
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from geoposition.fields import Geoposition



class ImporterTestCase(TestCase):

    def setUp(self):
        self.business = Business()

    def test_can_save_negative_string(self):
        latitude=-26.206820
        longitude = 28.038800
        self.business.id = 1
        self.business.location = Geoposition(latitude,longitude)
        self.business.save()
        self.assertEquals(self.business.id,1)















