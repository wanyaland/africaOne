#!/home/wanyama/workspace/africa_one/env/bin/python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","africa_one.settings")
import django
django.setup()
from geoposition.fields import Geoposition


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

'''
csv_listings ="/home/wanyama/workspace/africa_one/csv/Listing.csv"

business_reader = csv.reader(open(csv_listings),delimiter=',',quotechar='"')

for row in business_reader:
    #print row
    print row[6]+" "+row[7]
    business = Business()
    business.id = row[0]
    business.name=row[1]
    business.email=row[2]
    business.description=row[3]
    business.address=row[4]
    business.web_address=row[5]
    if not row[6] and not row[7]:
        pass
    else:
        business.location = Geoposition(row[6],row[7])
    business.phone_number=row[8]
    business.save()
    print "isdone"

'''


print "completed"

csv_category_listing ="/home/wanyama/workspace/africa_one/csv/Listing_Category.csv"

reader =csv.reader(open(csv_category_listing),delimiter=',',quotechar='"')

for row in reader:
    business = Business.objects.get(pk=row[0])
    category = Category.objects.get(pk=row[1])
    business.categories.add(category)
    business.save()
    print "saving" + business.name









