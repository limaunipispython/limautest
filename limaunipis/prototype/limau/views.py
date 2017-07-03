from operator import attrgetter
from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from limau.models import Recipe, Article, Restaurant
from limau.forms import UserForm, UserProfileForm

# Create your views here.
def index(request):
    template = loader.get_template('mainsite/index.html')
    page_template = loader.get_template('mainsite/index_entries.html')
    try:
        recipes = Recipe.objects.all()
        articles = Article.objects.all()
        restaurants = Restaurant.objects.all()
        content_list = sorted(chain(recipes, articles, restaurants), key=attrgetter('created_date'), reverse=True)
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

def recipe_all(request):
    template = loader.get_template('mainsite/recipe_all.html')
    page_template = loader.get_template('mainsite/recipe_entries.html')
    try:
        recipes = Recipe.objects.all().order_by('-created_date')
    except Recipe.DoesNotExist:
        return HttpResponse("Error 404")

    context = {
        'recipes' : recipes,
        'page_template' : page_template,
        'nbar' : "recipes"
    }

    if request.is_ajax():
        template = page_template
    return HttpResponse(template.render(context, request))

def article_all(request):
    template = loader.get_template('mainsite/article_all.html')
    page_template = loader.get_template('mainsite/article_entries.html')
    try:
        articles = Article.objects.all().order_by('-created_date')
    except Article.DoesNotExist:
        return HttpResponse("error 404")

    context = {
        'articles' : articles,
        'page_template' : page_template,
        'nbar' : "articles",
    }

    if request.is_ajax():
        template = page_template

    return HttpResponse(template.render(context, request))

def restaurant_all(request):
    template = loader.get_template('mainsite/restaurant_all.html')
    page_template = loader.get_template('mainsite/restaurant_entries.html')
    try:
        restaurants = Restaurant.objects.all().order_by('-created_date')
    except Restaurant.DoesNotExist:
        return HttpResponse("error 404")
    context = {
        'restaurants' : restaurants,
        'page_template' : page_template,
        'nbar' : "restaurants",
    }

    if request.is_ajax():
        template = page_template
    return HttpResponse(template.render(context, request))

def recipe_single(request, slug):
    template = loader.get_template('mainsite/recipe_single.html')
    try:
        recipe = Recipe.objects.get(slug=slug)
    except Recipe.DoesNotExist:
        return HttpResponse("error 404")
    context = {
        'recipe' : recipe,
        'nbar' : "recipes",
    }
    return HttpResponse(template.render(context, request))

def restaurant_single(request, slug):
    template = loader.get_template('mainsite/restaurant_single.html')
    try:
        restaurant = Restaurant.objects.get(slug=slug)
    except Restaurant.DoesNotExist:
        return HttpResponse("error 404")
    context = {
        'restaurant': restaurant,
        'nbar': "restaurants",
    }
    return HttpResponse(template.render(context, request))

def article_single(request, slug):
    template = loader.get_template('mainsite/article_single.html')
    try:
        article = Article.objects.get(slug=slug)
        recent_articles = Article.objects.all().order_by('-created_date')[:5]
    except article.DoesNotExist:
        return HttpResponse("error 404")
    context = {
        'recent_articles' : recent_articles,
        'article' : article,
        'nbar' : "articles",
    }
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

def register(request):
    template = loader.get_template('mainsite/register.html')
  
    # a boolean value to tell registration successful or not
    # initially set to false, true when succeed
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if profile_form.is_valid() == False:
            print("profile form is not valid")

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # since we need to define profile.user ourself
            # we delay the profile.save() into the database
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # render HTML form for the user to fill in
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered' : registered,
    }

    return HttpResponse(template.render(context, request))

    