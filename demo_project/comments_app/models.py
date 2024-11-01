from enum import Enum

from django.contrib.auth.models import User
from django.db import models


class CommentsAnchorType(Enum):
    POST = 1


class CommentsAnchor(models.Model):
    anchor_type = models.SmallIntegerField(
        choices=[(tag.value, tag.name) for tag in CommentsAnchorType]
    )


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    parent_comments_anchor = models.ForeignKey(
        CommentsAnchor, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=["parent_comments_anchor", "created_at"]),
        ]
