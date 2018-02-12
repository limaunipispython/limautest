from django import template
from limau.models import UserRecipe, MobileBanner, Announcement

register = template.Library()

@register.inclusion_tag('mainsite/user_recipe_tag.html')
def get_recent_user_recipe():
    return { 'user_recipe' : UserRecipe.objects.all().order_by('-created_date')[:5] }

@register.inclusion_tag('mainsite/social_media_tag.html')
def get_social_media():
    return { 'social_logo' : MobileBanner.objects.all() }

@register.inclusion_tag('mainsite/announcement_tag.html')
def get_announcement():
    return { 'announcement' : Announcement.objects.all().order_by('-created_date')}