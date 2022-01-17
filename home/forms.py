from django import forms
from django.contrib.auth.models import User
from userprofile.models import Profile
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email',
                  'first_name',
                  'last_name',
                  'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'mobile', 'address1', 'address2', 'city', 'state', 'country', 'zip']
