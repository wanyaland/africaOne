from django.test import TestCase
from models import Business,Review,Customer
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models



settings.RATINGS_VOTES_PER_IP=3



class ReviewsTestCase(TestCase):


    def setUp(self):
        self.user = User.objects.create(username='peter')
        self.user2 = User.objects.create(username='john')
        self.user3= User.objects.create(username='irene')
        self.business = Business.objects.create(name='javas')
        self.customer = Customer.objects.create(user=self.user)
        self.customer2=Customer.objects.create(user=self.user2)
        self.customere3 = Customer.objects.create(user=self.user3)
        self.review = Review.objects.create(customer=self.customer,business=self.business)
        self.review2 = Review.objects.create(customer=self.customer2,business=self.business)
        #self.review3 = Review.objects.create(customer=self.customere3,business=self.business)



    def test_can_get_no_reviews(self):
        self.review.rating.add(score=3,user=self.user,ip_address='127.0.0.1')
        self.review2.rating.add(score=2,user=self.user2,ip_address='127.0.0.1')
        self.assertEquals(self.review.rating.score,3)
        self.assertEqual(self.review.rating.votes,1)
        self.assertEquals(self.review2.rating.score,2)
        self.assertEquals(self.review2.rating.votes,1)
        self.assertEquals(self.business.get_no_reviews(),2)
        Review.objects.create(customer=self.customere3,business=self.business)
        self.assertEquals(self.business.get_no_reviews(),3)


        #get avg_business
        self.assertEquals(self.business.get_avg_rating(),(float)(3+2)/2)


















