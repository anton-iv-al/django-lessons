from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image_data = models.ImageField()
