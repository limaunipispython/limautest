"""prototype URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views import static
from limau import views

app_name = 'limau'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recipe_all/$', views.recipe_all, name="recipe_all"),
    url(r'^article_all/$', views.article_all, name="article_all"),
    url(r'^restaurant_all/$', views.restaurant_all, name="restaurant_all"),
    url(r'^recipe/(?P<slug>[\w\-]+)/$', views.recipe_single, name="recipe_single"),
    url(r'^restaurant/(?P<slug>[\w\-]+)/$', views.restaurant_single, name="restaurant_single"),
    url(r'^article/(?P<slug>[\w\-]+)/$', views.article_single, name="article_single"),
    url(r'^testpage_index/$', views.testpage_index, name="testpage_index"),
    url(r'^testpage_model/$', views.testpage_model, name="testpage_model"),
    url(r'^register/$', views.register, name="register"),   
    url(r'^login/$', views.user_login, name="login"),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^emailtest/$', views.emailtest, name="emailtest"),
    url(r'^userrecipeform/$', views.user_recipe_post, name="user_recipe_post"),
    url(r'^user_recipe/(?P<slug>[\w\-]+)/$', views.user_recipe_single, name="user_recipe_single"),
    url(r'^user_recipe/(?P<pk>\d+)/edit/$', views.user_recipe_edit, name="user_recipe_edit"),
    url(r'^user_recipe_all/$', views.user_recipe_all, name="user_recipe_all"),
    url(r'^user_profile/(?P<username>[\w\-]+)/$', views.user_profile, name="user_profile"),
    url(r'^user_profile_form/$', views.user_profile_form, name="user_profile_form"),
]

media_url = url(r'media/(?P<path>.*)', static.serve, {'document_root' : settings.MEDIA_ROOT}, name="media_folder")

if settings.DEBUG:
    urlpatterns.append(media_url)