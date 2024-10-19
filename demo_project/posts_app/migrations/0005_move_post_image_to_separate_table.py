# type: ignore

from django.apps.registry import Apps
from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def move_post_image(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    PostImage = apps.get_model("posts_app", "PostImage")
    Post = apps.get_model("posts_app", "Post")

    for post in Post.objects.all():
        if post.image:
            image = PostImage(post=post, image_data=post.image)
            image.save()
        post.image = None
        post.save()


class Migration(migrations.Migration):
    dependencies = [
        ("posts_app", "0004_postimage"),
    ]

    operations = [
        migrations.RunPython(move_post_image, migrations.RunPython.noop),
    ]
