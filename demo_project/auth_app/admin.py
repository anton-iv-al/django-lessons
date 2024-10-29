from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from media_app.models import Media

from . import models


class ProfileInline(admin.StackedInline):
    model = models.Profile

    def avatar_tag(self, obj):
        avatar = Media.objects.filter(id=obj.avatar_id).first()
        if avatar is None:
            return ""

        return format_html(
            f'<a href="{avatar.file.url}" target="_blank"><img src="{avatar.file.url}" width="100" height="100" /></a>'
        )

    fields = ["avatar", "avatar_tag", "phone", "about", "github_link"]
    readonly_fields = ["avatar_tag"]


admin.site.unregister(User)


@admin.register(User)
class UserProfileAdmin(UserAdmin):
    inlines = (ProfileInline,)
