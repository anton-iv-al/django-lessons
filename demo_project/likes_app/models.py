from enum import Enum

from django.contrib.auth.models import User
from django.db import models


class LikesAnchorType(Enum):
    POST = 1
    COMMENT = 2


class LikesAnchor(models.Model):
    anchor_type = models.SmallIntegerField(
        choices=[(tag.value, tag.name) for tag in LikesAnchorType]
    )


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    parent_likes_anchor = models.ForeignKey(
        LikesAnchor, on_delete=models.CASCADE, related_name="likes"
    )

    class Meta:
        unique_together = [("parent_likes_anchor", "user")]
