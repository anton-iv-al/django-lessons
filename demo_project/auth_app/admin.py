from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from . import models


class ProfileInline(admin.StackedInline):
    model = models.Profile


admin.site.unregister(User)


@admin.register(User)
class UserProfileAdmin(UserAdmin):
    inlines = (ProfileInline,)
