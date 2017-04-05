import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prototype.settings')

import django
django.setup()

from limau.models import Recipe, Article, Restaurant

def populate():
    for i in range(0, 7):
        myobj = Recipe.objects.all()[0]
        myobj.pk = None
        myobj.name_en = myobj.name_en + " " + str(i)
        myobj.name_bm = myobj.name_bm + " " + str(i)
        myobj.save()

    for i in range(0, 7):
        myobj = Article.objects.all()[0]
        myobj.pk = None
        myobj.title_bm = myobj.title_bm + " " + str(i)
        myobj.save()

    for i in range(0, 7):
        myobj = Restaurant.objects.all()[0]
        myobj.pk = None
        myobj.name_bm = myobj.name_bm + " " + str(i)
        myobj.save()


if __name__ == '__main__':
    print("starting limau population script..populating.....")
    populate()
