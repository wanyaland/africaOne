#!/home/wanyama/workspace/africa_one/env/bin/python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","africa_one.settings")
import django
django.setup()
from geoposition.fields import Geoposition
from django.db.models import URLField

import csv

csv_categories = "/home/wanyama/workspace/africa_one/csv/ListingCategory.csv"

from core.models import Category,Business

'''
dataReader = csv.reader(open(csv_categories),delimiter=',',quotechar='"')

for row in dataReader:
    category = Category()
    category.id=row[0]
    category.name= row[1]
    category.save()
    print category
    print "isdone"

print"Completed categories"
'''

csv_listings ="/home/wanyama/workspace/africa_one/csv/Listing.csv"

business_reader = csv.reader(open(csv_listings),delimiter=',',quotechar='"')

for row in business_reader:

    business = Business()
    business.id = row[0]
    business.name=row[1]
    business.description=row[2]
    business.web_address=row[4]
    business.location = Geoposition(row[5],row[6])
    business.phone_number=row[7]
    business.save()
    print "isdone"


print "completed"









