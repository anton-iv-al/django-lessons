from comments_app.models import CommentsAnchor
from django.contrib.auth.models import User
from django.db import models
from media_app.models import Media


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    comments_anchor = models.OneToOneField(
        CommentsAnchor, on_delete=models.PROTECT, related_name="post", null=True
    )


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image_data = models.ForeignKey(Media, on_delete=models.CASCADE)
