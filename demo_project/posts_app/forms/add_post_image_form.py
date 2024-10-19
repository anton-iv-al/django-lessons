from django import forms

from ..models import PostImage


class AddPostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ("image_data",)
