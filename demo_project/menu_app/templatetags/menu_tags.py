from typing import Any
from django import template
from django.utils.html import format_html

from ..models import Menu

register = template.Library()


@register.inclusion_tag("menu.html")
def main_menu():
    menu = Menu.objects.get(menu_label="main_menu")
    return {"menu": menu.links.order_by("priority").all()}


@register.inclusion_tag("menu.html", takes_context=True)
def user_menu(context: template.RequestContext):
    if context.request.user.is_authenticated:
        user: Any = context.request.user
        head = user.username
        if user.profile.avatar:
            head += format_html('<img src="{}" width="50" height="50" alt="User avatar">', user.profile.avatar.url)

        return {
            "head": head,
            "menu": [
                {"title": "User info", "url": "/auth/user/"},
                {
                    "title": "Logout",
                    "url": f"/auth/logout/?next={context.request.get_full_path()}",
                },
            ],
        }
    else:
        return {
            "menu": [
                {"title": "Login", "url": "/auth/login/"},
                {"title": "Registration", "url": "/auth/registration/"},
            ]
        }
