from django import forms

from ..models import Media


class CreateMediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ("file", "media_type")
