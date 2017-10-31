from django import template
from limau.models import UserRecipe

register = template.Library()

@register.inclusion_tag('mainsite/user_recipe_tag.html')
def get_recent_user_recipe():
    return { 'user_recipe' : UserRecipe.objects.all().order_by('-created_date')[:5] }