from django import forms

from ..models import Post


class EditPostForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = Post
        fields = ("username", "title", "text")
