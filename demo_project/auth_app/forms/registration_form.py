from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")

    def save(self, commit=True):
        user: User = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))

        if commit:
            user.save()

        return user
