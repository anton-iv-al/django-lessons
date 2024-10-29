from django.contrib.auth.models import User
from django.core import management
from django.core.management.base import BaseCommand
from menu_app.models import Menu, MenuItem


class Command(BaseCommand):
    help = "Run migrations and seed db."

    def handle(self, *args, **options):
        management.call_command("migrate")

        User.objects.create_superuser(
            username="admin",
            email="",
            password="admin",
            is_active=True,
            is_staff=True,
        )

        user1 = User()
        user1.username = "user1"
        user1.set_password("1234")
        user1.save()

        user2 = User()
        user2.username = "user2"
        user2.set_password("1234")
        user2.save()

        main_menu = Menu()
        main_menu.menu_label = "main_menu"
        main_menu.save()

        posts_menu_item = MenuItem()
        posts_menu_item.title = "Posts"
        posts_menu_item.url = "/post/"
        posts_menu_item.menu = main_menu
        posts_menu_item.save()

        tags_menu_item = MenuItem()
        tags_menu_item.title = "Tags"
        tags_menu_item.url = "/tag/"
        tags_menu_item.menu = main_menu
        tags_menu_item.save()

        media_menu_item = MenuItem()
        media_menu_item.title = "Media"
        media_menu_item.url = "/media/"
        media_menu_item.menu = main_menu
        media_menu_item.save()
