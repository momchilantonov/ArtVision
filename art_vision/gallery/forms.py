from art_vision.gallery.models import Image
from django import forms


class ImageForm(forms.ModelForm):
    class Meta:
        models = Image
        fields = '__all__'