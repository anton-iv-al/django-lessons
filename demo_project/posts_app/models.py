from typing import Any
from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=100)
    text = models.TextField()
    username = models.CharField(max_length=100, null=True, blank=True)

    tags: Any


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image_data = models.ImageField()
