from django.db import models


class PostTag(models.Model):
    id: int
    name = models.CharField(max_length=50, unique=True)
    count = models.PositiveIntegerField(default=0)
    posts = models.ManyToManyField("posts_app.Post", related_name="tags")

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["count"]),
        ]

    def __str__(self):
        return self.name
