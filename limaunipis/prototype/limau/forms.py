from django import forms
from django.contrib.auth.models import User
from limau.models import UserProfile, UserRecipe

class UserForm(forms.ModelForm):
    """Form definition for User."""
    # widget to assist HTML text input for password
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    """Form definition for UserProfile."""
    # no widget defined for the picture attributes

    class Meta:
        """Meta definition for UserProfileform."""

        model = UserProfile
        fields = ('picture', 'description')


class UserRecipeForm(forms.ModelForm):
    # no widget 

    class Meta: 
        model = UserRecipe
        fields = ('recipecategory', 'name_bm', 'name_en', 'description', 'content', 'picture_1', 'picture_2')
