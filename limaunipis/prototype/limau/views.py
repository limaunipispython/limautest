from operator import attrgetter
from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from limau.models import Recipe, Article, Restaurant


# Create your views here.
def index(request):
    template = loader.get_template('mainsite/index.html')
    page_template = loader.get_template('mainsite/index_entries.html')
    try:
        recipes = Recipe.objects.all()
        articles = Article.objects.all()
        restaurants = Restaurant.objects.all()
        content_list = sorted(chain(recipes, articles, restaurants), key=attrgetter('created_date'))
    except (Recipe.DoesNotExist, Article.DoesNotExist, Restaurant.DoesNotExist):
        return HttpResponse("Error 404")
    context = {
        'content_list' : content_list,
        'page_template' : page_template,
        'nbar' : "home",
    }
    if request.is_ajax():
        template = page_template
    return HttpResponse(template.render(context, request))

def testpage_index(request):
    template = loader.get_template('mainsite/testpage_index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def testpage_model(request):
    template = loader.get_template('mainsite/testpage_model.html')
    try:
        recipes = Recipe.objects.all()
        articles = Article.objects.all()
        restaurants = Restaurant.objects.all()
        content_list = sorted(chain(recipes, articles, restaurants), key=attrgetter('created_date'))
    except (Recipe.DoesNotExist, Article.DoesNotExist, Restaurant.DoesNotExist):
        return HttpResponse("Error 404")

    context = {
        'content_list' : content_list,
    }
    return HttpResponse(template.render(context, request))
