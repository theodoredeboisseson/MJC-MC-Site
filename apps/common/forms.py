from django import forms
from wagtail.images.models import Image
from .widgets import RepositionableImageWidget

class CustomImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        widgets = {
            'file': RepositionableImageWidget(),
        }