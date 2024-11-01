from comments_app.models import Comment
from common.decorators.disable_signal_for_loaddata import disable_signal_for_loaddata
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from posts_app.models import Post

from likes_app.models import LikesAnchor, LikesAnchorType


@receiver(post_save, sender=Post)
@disable_signal_for_loaddata
def add_likes_anchor_to_post(sender, instance: Post, created, *args, **kwargs):
    if not created:
        return

    anchor = LikesAnchor(anchor_type=LikesAnchorType.POST.value)
    anchor.save()
    instance.likes_anchor = anchor
    instance.save()


@receiver(post_delete, sender=Post)
@disable_signal_for_loaddata
def delete_likes_anchor_from_post(sender, instance: Post, *args, **kwargs):
    if instance.likes_anchor is not None:
        instance.likes_anchor.delete()


@receiver(post_save, sender=Comment)
@disable_signal_for_loaddata
def add_likes_anchor_to_comment(sender, instance: Comment, created, *args, **kwargs):
    if not created:
        return

    anchor = LikesAnchor(anchor_type=LikesAnchorType.COMMENT.value)
    anchor.save()
    instance.likes_anchor = anchor
    instance.save()


@receiver(post_delete, sender=Comment)
@disable_signal_for_loaddata
def delete_likes_anchor_from_comment(sender, instance: Comment, *args, **kwargs):
    if instance.likes_anchor is not None:
        instance.likes_anchor.delete()
