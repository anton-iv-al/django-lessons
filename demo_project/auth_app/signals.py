from common.decorators.disable_signal_for_loaddata import disable_signal_for_loaddata
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
@disable_signal_for_loaddata
def create_profile(sender, instance, created, *args, **kwargs):
    if not created:
        return

    profile = Profile(user=instance)
    profile.save()
