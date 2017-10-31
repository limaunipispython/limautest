import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prototype.settings')

import django
django.setup()

from limau.models import UserRecipe
from datetime import timedelta

def populate():
    for i in range(0, 15):
        user_recipe = UserRecipe.objects.all()[0]
        user_recipe.pk = None
        user_recipe.name_bm = user_recipe.name_bm + " " + str(i)
        user_recipe.name_en = user_recipe.name_en + " " + str(i)
        user_recipe.save()

def populate_time():
    user_recipe = UserRecipe.objects.all()
    for index in range(len(user_recipe)):
        user_recipe[index].created_date = user_recipe[index].created_date + timedelta(days = index + 1)
        user_recipe[index].save()


if __name__ == "__main__":
    print("start populating user recipes")
    populate()
    populate_time()