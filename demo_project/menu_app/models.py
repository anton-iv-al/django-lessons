from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Menu(models.Model):
    menu_label = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"{self.id} {self.menu_label}"


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT, related_name="links")
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    icon = models.ImageField(null=True, blank=True)
    priority = models.FloatField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
        help_text="Lower numbers are shown first",
    )

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        indexes = [
            models.Index(fields=("menu",)),
            models.Index(fields=("menu", "url")),
        ]
        unique_together = [("menu", "title")]
