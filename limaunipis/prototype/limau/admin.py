from django.contrib import admin
from limau.models import RecipeCategory, ArticleCategory, RestaurantCategory, Ingredient, Recipe, Article, Restaurant

# Register your models here.

admin.site.register(RecipeCategory)
admin.site.register(ArticleCategory)
admin.site.register(RestaurantCategory)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Article)
admin.site.register(Restaurant)