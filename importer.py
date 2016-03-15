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
    print row

    business = Business()
    business.id = row[0]
    business.name=row[1]
    business.email=row[2]
    business.description=row[3]
    business.web_address=row[5]
    business.location = Geoposition(row[7],row[8])
    business.phone_number=row[9]
    business.save()
    print "isdone"



print "completed"









