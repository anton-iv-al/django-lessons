# Generated by Django 5.1.2 on 2024-11-01 12:18

from django.apps.registry import Apps
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
import django.db.models.deletion
from django.db import migrations, models

def create_comments_anchors_for_existing_posts(
    apps: Apps, schema_editor: BaseDatabaseSchemaEditor
):
    post_model = apps.get_model("posts_app", "Post")
    anchor_model = apps.get_model("comments_app", "CommentsAnchor")

    posts = post_model.objects.filter(comments_anchor__isnull=True)
    for post in posts:
        anchor = anchor_model(anchor_type=1)
        anchor.save()
        post.comments_anchor = anchor
        post.save()

def delete_comments_anchors_from_posts(
    apps: Apps, schema_editor: BaseDatabaseSchemaEditor
):    
    post_model = apps.get_model("posts_app", "Post")

    posts = post_model.objects.filter(likes_anchor__isnull=False)
    for post in posts:
        anchor = post.comments_anchor
        post.comments_anchor = None
        post.save()
        anchor.delete()
    
class Migration(migrations.Migration):

    dependencies = [
        ('comments_app', '0001_initial'),
        ('posts_app', '0008_alter_postimage_image_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments_anchor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='post', to='comments_app.commentsanchor'),
        ),

        migrations.RunPython(create_comments_anchors_for_existing_posts, delete_comments_anchors_from_posts),
    ]
