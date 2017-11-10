from operator import attrgetter
from itertools import chain
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from limau.models import Recipe, Article, Restaurant, UserRecipe
from limau.forms import UserForm, UserProfileForm, UserRecipeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.mail import EmailMessage
from django.contrib.auth.models import User


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

def user_recipe_all(request):
    template = loader.get_template('mainsite/user_recipe_all.html')
    page_template = loader.get_template('mainsite/user_recipe_entries.html')
    try:
        recipes = UserRecipe.objects.all().order_by('-created_date')
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

# registration view
def register(request):
    template = loader.get_template('mainsite/register.html')
  
    # a boolean value to tell registration successful or not
    # initially set to false, true when succeed
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

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

# Login Page view
def user_login(request):
    template = loader.get_template('mainsite/login.html')
    context = {}

    if request.method == 'POST':
        # 'username' should be based on input name in html
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(user)

        # if user found in the database it well return True 
        if user:
            # user account might be disabled
            if user.is_active:
                login(request, user)
                # reverse is required to obtain URL
                return HttpResponseRedirect(reverse('limau:index'))
            else:
                return HttpResponse("Your Account is disabled, please contact administrator")
        else: 
            print("invalid login details: {0}, {1} ".format(username, password))
            # better to create a template for wrong login and use HttpResponseRedirect
            return HttpResponse("Invalid login details supplied")
    else:
        return HttpResponse(template.render(context, request))

# USER RECIPE VIEW
#need to include decorator to only allow authenticated user to access
@login_required
def user_recipe_post(request):
    template = loader.get_template('forms/userrecipeform.html')
    if request.method == "POST":
        form = UserRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            if 'picture_1' in request.FILES:
                post.picture_1  = request.FILES['picture_1']
            if 'picture_2' in request.FILES:
                post.picture_2 = request.FILES['picture_2']
            post.save()
            return redirect('limau:user_recipe_single', slug=post.slug)
    else:   
        form = UserRecipeForm()
    context = {
        'form' : form,
    }

    return HttpResponse(template.render(context,request))

#single user recipe view
def user_recipe_single(request, slug):
    template = loader.get_template('mainsite/user_recipe_single.html')

    try:
        user_recipe = UserRecipe.objects.get(slug=slug)
        latest_recipe = UserRecipe.objects.filter(user=user_recipe.user).order_by('-created_date')[:5]
    except UserRecipe.DoesNotExist:
        return HttpResponse("error 404")
    context = {
        'user_recipe' : user_recipe,
        'latest_recipe': latest_recipe,
        'nbar' : 'recipes',
    }
    return HttpResponse(template.render(context, request))

def user_recipe_edit(request, pk):
    user_recipe = get_object_or_404(UserRecipe, pk=pk)
    template = loader.get_template('forms/userrecipeform_edit.html') # the problem is here since the user submit button submit to user recipe post
    if request.method == 'POST':
        form = UserRecipeForm(request.POST, request.FILES, instance = user_recipe)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            if 'picture_1' in request.FILES:
                post.picture_1 = request.FILES['picture_1']
            if 'picture_2' in request.FILES:
                post.picture_2 = request.FILES['picture_2']
            post.save()
            return redirect('limau:user_recipe_single', slug=post.slug)
        
    form = UserRecipeForm(instance = user_recipe)
    context = {
        'form' : form,
    }
    return HttpResponse(template.render(context, request))

# USER PROFILE SECTION

def user_profile(request, username):
    template = loader.get_template('mainsite/user_profile.html')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse("error 404")

    context = {
        'user' : user,
    }
    return HttpResponse(template.render(context, request))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('limau:index'))

# email testing
def emailtest(request):
    email = EmailMessage('Limau Nipis Password Recovery', 'Your password is this and this', to=['muzakkirm1988@gmail.com'])
    email.send()
    return HttpResponse("sending email")
   