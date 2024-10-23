from django.contrib import admin
from django.utils.html import format_html

from demo_project import settings

from . import models


class PostImageInline(admin.StackedInline):
    model = models.PostImage
    max_num = settings.MAX_IMAGES_FOR_POST

    def image_tag(self, obj):
        return format_html(
            f'<a href="{obj.image_data.url}" target="_blank"><img src="{obj.image_data.url}" width="200" height="200" /></a>'
        )

    list_display = ["image_tag"]
    readonly_fields = ["image_tag"]


@admin.register(models.Post)
class Post(admin.ModelAdmin):
    inlines = (PostImageInline,)
