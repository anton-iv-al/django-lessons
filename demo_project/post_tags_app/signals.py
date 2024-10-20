import re

from django.db.models.signals import post_save
from django.dispatch import receiver

from posts_app.models import Post
from .models import PostTag

hashtags_pattern = re.compile(r"(?<=#)\w+")


@receiver(post_save, sender=Post)
def add_post_tags(sender, instance: Post, created, *args, **kwargs):
    hashtags = hashtags_pattern.findall(instance.text)

    old_tags = set(instance.tags.all())

    new_tags = set()
    for tag_name in hashtags:
        if len(tag_name) > PostTag._meta.get_field("name").max_length:
            continue

        tag, _ = PostTag.objects.get_or_create(name=tag_name, defaults={"count": 0})
        new_tags.add(tag)

    for tag in new_tags - old_tags:
        instance.tags.add(tag)
        tag.count += 1
        tag.save()

    for tag in old_tags - new_tags:
        instance.tags.remove(tag)
        tag.count -= 1
        if tag.count == 0:
            tag.delete()
        else:
            tag.save()
