from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(null=True)
