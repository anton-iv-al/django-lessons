from django.apps.registry import Apps
from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def create_profiles_for_existing_users(
    apps: Apps, schema_editor: BaseDatabaseSchemaEditor
):
    user_model = apps.get_model("auth", "User")
    profile_model = apps.get_model("auth_app", "Profile")

    users = user_model.objects.filter(profile__isnull=True).all()
    for user in users:
        profile = profile_model(user=user)
        profile.save()


class Migration(migrations.Migration):
    dependencies = [("auth_app", "0001_initial")]

    operations = [
        migrations.RunPython(create_profiles_for_existing_users, migrations.RunPython.noop),
    ]
