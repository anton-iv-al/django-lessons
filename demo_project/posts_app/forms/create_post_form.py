from django import forms

from demo_project import settings

from ..models import Post, PostImage


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text")


PostImageFormSet = forms.inlineformset_factory(
    Post, PostImage, fields="__all__", extra=settings.MAX_IMAGES_FOR_POST
)
