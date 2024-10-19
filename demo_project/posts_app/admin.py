from django.contrib import admin

from posts_app import settings as app_settings

from . import models


class PostImageInline(admin.StackedInline):
    model = models.PostImage
    max_num = app_settings.MAX_IMAGES_FOR_POST


@admin.register(models.Post)
class Post(admin.ModelAdmin):
    inlines = (PostImageInline,)
