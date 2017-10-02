jimport os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prototype.settings')

import django
django.setup()

from limau.models import Recipe, Article, Restaurant
from datetime import timedelta

recipes = Recipe.objects.all()
articles = Article.objects.all()
restaurants = Restaurant.objects.all()

def populate():
    for index in range(len(recipes)):
        recipes[index].created_date = recipes[index].created_date - timedelta(days=index+1)
        recipes[index].save()
    for index in range(len(restaurants)):
        restaurants[index].created_date = restaurants[index].created_date - timedelta(days=index+1)
        restaurants[index].save()
    for index in range(len(articles)):
        articles[index].created_date = articles[index].created_date - timedelta(days=index+1)
        articles[index].save()

if __name__ == '__main__':
    print("starting limau population script..populating.....")
    populate()
