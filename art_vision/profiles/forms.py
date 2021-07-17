from django import forms
from django.forms import fields
from art_vision.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'is_completed')