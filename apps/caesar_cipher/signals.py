from django.db.models.signals import post_delete
from django.dispatch import receiver

from apps.caesar_cipher import models


@receiver(post_delete, sender=models.Message)
def my_handler(
    sender: type[models.Message],
    instance: models.Message,
    **kwargs,
):
    instance.key.delete()
