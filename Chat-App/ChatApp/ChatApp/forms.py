from django import forms
from django.utils.translation import gettext as _

from ChatApp.models import Profile

class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["address", "photo"]
