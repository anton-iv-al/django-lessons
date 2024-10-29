from enum import Enum

from django.contrib.auth.models import User
from django.db import models


class MediaType(Enum):
    IMAGE = 1


class Media(models.Model):
    file = models.FileField()
    media_type = models.PositiveSmallIntegerField(
        choices=[(t.value, t.name) for t in MediaType]
    )
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_media_type_display(self):
        return MediaType(self.media_type).name
