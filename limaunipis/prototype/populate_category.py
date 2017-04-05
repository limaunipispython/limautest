import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prototype.settings')

import django
django.setup()


from limau.models import RecipeCategory, RestaurantCategory, ArticleCategory
# description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"

def addRecipeCat(name_bm, name_en, description):
    new_cat = RecipeCategory.objects.get_or_create(name_en=name_en)[0]
    new_cat.name_bm = name_bm
    new_cat.description = description
    new_cat.save()

def addArticleCat(name_bm, name_en, description):
    new_cat = ArticleCategory.objects.get_or_create(name_en=name_en)[0]
    new_cat.name_bm = name_bm
    new_cat.description = description
    new_cat.save()

def addRestaurantCat(name_bm, name_en, description):
    new_cat = RestaurantCategory.objects.get_or_create(name_en=name_en)[0]
    new_cat.name_bm = name_bm
    new_cat.description = description
    new_cat.save()

def populate():
    description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"

    addRecipeCat("Melayu", "Malay", description=description)
    addRecipeCat("Barat", "Western", description=description)
    addRecipeCat("Asia", "Asian", description=description)

    addArticleCat("Umum", "General", description=description)
    addArticleCat("Makanan Kesihatan", "Health Food", description=description)
    addArticleCat("Makanan Bayi", "Baby Food", description=description)

    addRestaurantCat("Melayu", "Malay", description=description)
    addRestaurantCat("Mewah", "Fine Dining", description=description)
    addRestaurantCat("Barat", "Western", description=description)
    addRestaurantCat("Thailand", "Thailand", description=description)
    addRestaurantCat("Jepun", "Japanese", description=description)


if __name__ == '__main__':
    print("starting limau population script..populating.....")
    populate()
