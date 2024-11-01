from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from posts_app.models import Post

from comments_app.models import CommentsAnchor, CommentsAnchorType


@receiver(post_save, sender=Post)
def add_comments_anchor(sender, instance: Post, created, *args, **kwargs):
    if not created:
        return

    anchor = CommentsAnchor(anchor_type=CommentsAnchorType.POST.value)
    anchor.save()
    instance.comments_anchor = anchor
    instance.save()


@receiver(post_delete, sender=Post)
def delete_comments_anchor(sender, instance: Post, *args, **kwargs):
    if instance.comments_anchor is not None:
        instance.comments_anchor.delete()
