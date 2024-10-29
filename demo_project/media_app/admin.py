from django.contrib import admin
from django.utils.html import format_html

from .models import Media, MediaType


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "media_tag", "media_type", "created_at", "user")
    readonly_fields = ("media_tag",)

    def media_tag(self, obj):
        if obj.media_type == MediaType.IMAGE.value:
            return format_html(
                f'<a href="{obj.file.url}" target="_blank"><img src="{obj.file.url}" width="200" height="200" /></a>'
            )
        return ""
