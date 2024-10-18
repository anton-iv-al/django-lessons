from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(null=True, blank=True)
    phone = models.CharField(
        validators=[RegexValidator(r"^\+?[1-9][0-9]{7,14}$")],
        max_length=17,
        null=True,
        blank=True,
    )
    about = models.TextField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
