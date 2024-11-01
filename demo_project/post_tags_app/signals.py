import re

from common.decorators.disable_signal_for_loaddata import disable_signal_for_loaddata
from django.db.models.signals import post_save
from django.dispatch import receiver
from posts_app.models import Post

from .models import PostTag

hashtags_pattern = re.compile(r"(?<=#)\w+")


@receiver(post_save, sender=Post)
@disable_signal_for_loaddata
def add_post_tags(sender, instance: Post, created, *args, **kwargs):
    hashtags = set(hashtags_pattern.findall(instance.text))

    old_tags = {tag.name: tag for tag in instance.tags.all()}

    for tag_name in hashtags - old_tags.keys():
        if len(tag_name) > PostTag._meta.get_field("name").max_length:
            continue

        tag, created = PostTag.objects.get_or_create(
            name=tag_name,
            defaults={"count": 1},
        )
        if not created:
            tag.count += 1
            tag.save()
        instance.tags.add(tag)

    for tag_name in old_tags.keys() - hashtags:
        tag = old_tags[tag_name]
        instance.tags.remove(tag)
        tag.count -= 1
        if tag.count == 0:
            tag.delete()
        else:
            tag.save()
