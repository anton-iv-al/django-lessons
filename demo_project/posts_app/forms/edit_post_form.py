from django import forms

from ..models import Post


class EditPostForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].initial = self.instance.user.username

    class Meta:
        model = Post
        fields = ("username", "title", "text")
