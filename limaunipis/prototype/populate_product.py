import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prototype.settings')

import django
django.setup()

from limau.models import Product
from datetime import timedelta

def populate():
    for i in range(0, 25):
        item = Product.objects.get(pk=28)
        item.pk = None
        item.name = item.name + str(i)
        item.save()

def populate_time():
    items = Product.objects.all()
    for index in range(len(items)):
        items[index].created_date = items[index].created_date + timedelta(days = index + 1)
        items[index].save()

if __name__ == "__main__":
    print("start populating products by repeating the first product entry")
    populate()
    populate_time()